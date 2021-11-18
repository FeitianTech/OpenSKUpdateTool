# This Python file uses the following encoding: utf-8
import os
import sys
import click
import threading
from enum import IntEnum, unique
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtCore import QSharedMemory, QCoreApplication, Qt, pyqtSignal
from update_tool import Ui_UpdateTool
from device import FIDODevice
from certificate import Certificate
from nordicsemi.dfu.dfu_transport_serial import DfuTransportSerial, DfuEvent
from nordicsemi.dfu.dfu import Dfu
from nordicsemi.lister.device_lister import DeviceLister


# Prompt message
MSG_VERSION = 'V1.0.1'
MSG_NOT_BOOTLOADER = 'Please switch OpenSK to bootloader mode.'
MSG_BOOTLOADER = 'Please switch OpenSK to working mode.'
MSG_ERASE_WAITING = 'Erasing firmware, please wait...'
MSG_ERASE_SUCCESS = 'Erase firmware successfully.'
MSG_UPDATE_NO_ZIP = 'Not found nrf52840_dongle_dfu_dfu.zip'
MSG_UPDATE_WAITING = 'Burning firmware, please wait...'
MSG_UPDATE_SUCCESS = 'Firmware burning succeeded.'
MSG_CERT_NO_KEY = 'Not found crypto_data/opensk.key'
MSG_CERT_NO_PEM = 'Not found crypto_data/opensk_cert.pem'
MSG_CERT_WAIT_KEYDOWN = 'Press the user button...'
MSG_CERT_SUCCESS = 'Certificate updated successfully.'
MSG_BOX_TEXT = 'Attention please, both firmware and data will be erased.'


# Prompt message type
@unique
class ERRSTATE(IntEnum):
    NONE = 0xFF
    HIDE = 0x00
    SUCCESS = 0x01
    INFO = 0x02
    ERROR = 0x03
    WAITING = 0x04

#main window.
class MainWindow(QWidget, Ui_UpdateTool):
    signal = pyqtSignal(int, str)

    def __init__(self):
        super(MainWindow,self).__init__()
        self.state = ERRSTATE.NONE
        self.setupUi(self)
        self.widget_device.hide()
        self.widget_main.hide()
        self.show_result(ERRSTATE.HIDE)
        self.mFIDODevice = FIDODevice()
        self.signal.connect(self.show_result)

    def change_ui(self, enable):
        self.widget_main.setEnabled(enable)
        self.btn_refresh.setEnabled(enable)
        self.btn_inject.setEnabled(enable)
        self.btn_flash.setEnabled(enable)
        self.btn_update.setEnabled(enable)

    @staticmethod
    def runtime_path(relative_path):
        if sys.platform == "darwin":
            dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))
            if relative_path == '':
                return dirname + '/../../../'
            else:
                base_path = dirname+'/../Resources'
        else:
            if relative_path == '':
                return ''
            base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

        return os.path.join(base_path, relative_path)

    @staticmethod
    def check_com_authority():
        # Upgrade COM port permissions
        cmd = "pkexec --user root chmod 777 /dev/ttyACM*"
        os.system(cmd)

    @staticmethod
    def check_rules_authority():
        # Add rules permissions for using hid protocol.
        if not os.path.exists("/etc/udev/rules.d/55-opensk.rules"):
            cmd =  """pkexec --user root bash -c 'echo \"SUBSYSTEM==\\\"hidraw\\\", SUBSYSTEMS==\\\"usb\\\", """
            cmd += """ATTRS{idVendor}==\\\"1915\\\", ATTRS{idProduct}==\\\"521f\\\", ATTRS{product}==\\\"OpenSK\\\", """
            cmd += """MODE=\\\"0777\\\", GROUP=\\\"logindev\\\", TAG+=\\\"uaccess\\\"\" > /etc/udev/rules.d/55-opensk.rules"""
            cmd += """;udevadm control --reload '"""
            os.system(cmd)

    def get_fido_info(self, device):
        try:
            names = globals()
            if self.hl_fido_info.count() > 0:
                for i in range(self.hl_fido_info.count()):
                    self.hl_fido_info.itemAt(i).widget().deleteLater()

            self.mFIDODevice.open(device)
            fido_info = self.mFIDODevice.get_info()
            for i in range(len(fido_info.versions)):
                names["lab_version_{}".format(i)] = QLabel(fido_info.versions[i])
                names["lab_version_{}".format(i)].setStyleSheet(
                    "QLabel{background:rgb(0, 170, 0);font:9pt;color: rgb(255,255,255);border-radius:3px;}")
                self.hl_fido_info.addWidget(names["lab_version_{}".format(i)])
            for i in range(len(fido_info.extensions)):
                names["lab_extensions_{}".format(i)] = QLabel(fido_info.extensions[i])
                names["lab_extensions_{}".format(i)].setStyleSheet(
                    "QLabel{background: rgb(218,133,48);font:9pt;color: rgb(255,255,255);border-radius: 3px;}")
                self.hl_fido_info.addWidget(names["lab_extensions_{}".format(i)])
            for i in range(len(fido_info.transports)):
                names["lab_transports_{}".format(i)] = QLabel(fido_info.transports[i])
                names["lab_transports_{}".format(i)].setStyleSheet(
                    "QLabel{background: rgb(21,125,189);font:9pt;color: rgb(255,255,255);border-radius: 3px;}")
                self.hl_fido_info.addWidget(names["lab_transports_{}".format(i)])
        except Exception:
            pass

    def update_progress(self, progress=0):
        if global_bar:
            global_bar.update(progress)
            self.signal.emit(ERRSTATE.WAITING, global_bar.format_progress_line())

    # Call nrfutil third-party library to upgrade or delete firmware
    def firmware_nrfutil(self, package, serial_number):
        device_lister = DeviceLister()
        device = device_lister.get_device(serial_number=serial_number)
        if device is None:
            raise Exception("A device with serial number {0} is not connected.".format(serial_number))

        ping = False
        port = device.get_first_available_com_port()
        timeout = DfuTransportSerial.DEFAULT_TIMEOUT
        baud_rate = DfuTransportSerial.DEFAULT_BAUD_RATE
        flow_control = DfuTransportSerial.DEFAULT_FLOW_CONTROL
        packet_receipt_notification = DfuTransportSerial.DEFAULT_PRN
        serial_backend = DfuTransportSerial(com_port=str(port), baud_rate=baud_rate,
                                            flow_control=flow_control, prn=packet_receipt_notification,
                                            do_ping=ping,
                                            timeout=timeout)
        serial_backend.register_events_callback(DfuEvent.PROGRESS_EVENT, self.update_progress)
        dfu = Dfu(zip_file_path=package, dfu_transport=serial_backend, connect_delay=None)

        with click.progressbar(length=dfu.dfu_get_total_size()) as bar:
            global global_bar
            global_bar = bar
            dfu.dfu_send_images()

    def show_result(self, state, msg=''):
        if self.state != state:
            self.state = state
            if state == ERRSTATE.HIDE:
                self.widget_result.hide()
                return
            elif state == ERRSTATE.SUCCESS:
                self.lab_result_image.setPixmap(QPixmap(":/png/update_images/success.png"))
            elif state == ERRSTATE.INFO:
                self.lab_result_image.setPixmap(QPixmap(":/png/update_images/info.png"))
            elif state == ERRSTATE.ERROR:
                self.lab_result_image.setPixmap(QPixmap(":/png/update_images/error.png"))
            elif state == ERRSTATE.WAITING:
                movie = QMovie(":/png/update_images/loading.gif")
                self.lab_result_image.setMovie(movie)
                movie.start()
            else:
                return

        self.lab_result_msg.setText(msg.replace('\n', '').replace('\r\n', ''))
        if state != ERRSTATE.HIDE and self.widget_result.isHidden():
            self.widget_result.show()

    def tab_widget_clicked(self):
        self.show_result(ERRSTATE.HIDE)

    def erase_firmware_for_thread(self):
        try:
            self.change_ui(False)
            product_name, serial_number, device = self.mFIDODevice.find()
            if device:
                self.signal.emit(ERRSTATE.ERROR, MSG_NOT_BOOTLOADER)
                return
            if sys.platform == "linux":
                self.check_com_authority()

            self.signal.emit(ERRSTATE.WAITING, MSG_ERASE_WAITING)
            self.firmware_nrfutil(self.runtime_path('nrf52840_dongle_erase_dfu.zip'), serial_number)
            self.signal.emit(ERRSTATE.SUCCESS, MSG_ERASE_SUCCESS)
        except Exception as e:
            # OpenSK device not found
            self.signal.emit(ERRSTATE.ERROR, str(e))
        finally:
            self.change_ui(True)

    def update_certificate_for_thread(self):
        try:
            product_name, serial_number, device = self.mFIDODevice.find()
            if not device:
                self.signal.emit(ERRSTATE.ERROR, MSG_BOOTLOADER)
                return

            key_dir = self.runtime_path('') + './crypto_data/opensk.key'
            pem_dir = self.runtime_path('') + './crypto_data/opensk_cert.pem'
            if not os.path.exists(key_dir):
                self.signal.emit(ERRSTATE.ERROR, MSG_CERT_NO_KEY)
                return
            if not os.path.exists(pem_dir):
                self.signal.emit(ERRSTATE.ERROR, MSG_CERT_NO_PEM)
                return

            self.change_ui(False)
            self.signal.emit(ERRSTATE.WAITING, MSG_CERT_WAIT_KEYDOWN)
            m_certificate = Certificate()
            m_certificate.update(pem_dir, key_dir)
            self.signal.emit(ERRSTATE.SUCCESS, MSG_CERT_SUCCESS)
        except Exception as e:
            # OpenSK device not found
            self.signal.emit(ERRSTATE.ERROR, str(e))
        finally:
            self.change_ui(True)

    def update_firmware_for_thread(self):
        try:
            self.change_ui(False)
            product_name, serial_number, device = self.mFIDODevice.find()
            if device:
                self.signal.emit(ERRSTATE.ERROR, MSG_NOT_BOOTLOADER)
                return

            if sys.platform == "linux":
                self.check_com_authority()

            dfufile = self.runtime_path('') + './nrf52840_dongle_dfu_dfu.zip'

            if not os.path.exists(dfufile):
                self.signal.emit(ERRSTATE.ERROR, MSG_UPDATE_NO_ZIP)
                return

            self.signal.emit(ERRSTATE.WAITING, MSG_UPDATE_WAITING)
            self.firmware_nrfutil(dfufile, serial_number)
            self.signal.emit(ERRSTATE.SUCCESS, MSG_UPDATE_SUCCESS)
        except Exception as e:
            # OpenSK device not found
            self.signal.emit(ERRSTATE.ERROR, str(e))
        finally:
            self.change_ui(True)

    # Enumerate devices. Now only one device can be inserted
    def refresh_device(self):
        try:
            product_name, serial_number, device = self.mFIDODevice.find()
            self.lab_dev_mode.setText(product_name)
            self.lab_manufacture.setText(product_name)
            if serial_number is not None:
                self.lab_serial.setText('Serial: ' + serial_number)
            else:
                if type(device.descriptor.path) == bytes:
                    path = bytes.decode(device.descriptor.path)
                else:
                    path = device.descriptor.path
                self.lab_serial.setText(path)

            self.widget_device.show()
            self.widget_main.show()
            self.show_result(ERRSTATE.HIDE)
            if sys.platform == "linux":
                self.check_rules_authority()
            self.get_fido_info(device)
        except Exception as e:
            self.widget_device.hide()
            self.widget_main.hide()
            self.show_result(ERRSTATE.ERROR, str(e))

    def update_certificate(self):
        t1 = threading.Thread(target=self.update_certificate_for_thread)
        t1.start()

    def erase_firmware(self):
        msg_box = QMessageBox(QMessageBox.Question, 'warning', MSG_BOX_TEXT)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setWindowIcon(QIcon(":/png/update_images/icon.png"))
        if msg_box.exec_() == QMessageBox.No:
            return

        t1 = threading.Thread(target=self.erase_firmware_for_thread)
        t1.start()

    def update_firmware(self):
        t1 = threading.Thread(target=self.update_firmware_for_thread)
        t1.start()


if __name__ == "__main__":
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app = QApplication([])
    share = QSharedMemory()
    share.setKey("openSK_update_tool")
    if share.attach():
        sys.exit(-1)
    if share.create(1):
        window = MainWindow()
        window.setWindowTitle('OpenSK Update Tool    ' + MSG_VERSION)
        window.setWindowIcon(QIcon(":/png/update_images/icon.png"))
        window.refresh_device()
        window.show()
        sys.exit(app.exec_())
