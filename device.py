# encoding: utf-8

# author: LY
# license: Feitian Technologies Co., Ltd. 2019-2022
# file: device.py
# time: 2021-10-20 15:03
# desc:
from fido2.hid import CtapHidDevice
from fido2.ctap2 import CTAP2, PinProtocolV1, ClientPin
from nordicsemi.lister import device_lister
from threading import Timer


class FIDODevice:
    def __init__(self):
        self.dev = None
        self.ctap = None
        self.pin = None
        self._info = None
        self._pin = False

    def find(self):
        devices = []
        for dev in CtapHidDevice.list_devices():
            devices.append(dev)
        if len(devices) == 1:
            product_name = devices[0].descriptor.product_name
            serial_number = devices[0].descriptor.serial_number
            return product_name, serial_number, devices[0]
        elif len(devices) > 1:
            raise Exception("Multiple devices are detected. Please only connect one.")

        serial_number = []
        for device in device_lister.DeviceLister().enumerate():
            if device.vendor_id == "1915" and device.product_id == "521F":
                serial_number.append(device.serial_number)
        if not serial_number:
            raise Exception("Please insert your OpenSK USB Dongle.")
        if len(serial_number) > 1:
            raise Exception("Multiple OpenSK USB Dongles are detected. Please only connect one.")
        return 'OpenSK', serial_number[0], None

    def open(self, dev):
        try:
            self.dev = dev
            self.ctap = CTAP2(dev)
            self.pin = ClientPin(self.ctap, PinProtocolV1())
            self._info = self.ctap.get_info()
            self._pin = self._info.options['clientPin']
        except Exception as e:
            raise Exception(str(e))

    def get_info(self):
        return self._info

    def get_pin_retries(self):
        return self.pin.get_pin_retries()

    def set_pin(self, pin):
        self.pin.set_pin(pin)
        self._pin = True

    def change_pin(self, old_pin, new_pin):
        self.pin.change_pin(old_pin, new_pin)

    def reset(self, touch_callback=None):
        if (touch_callback):
            touch_timer = Timer(0.500, touch_callback)
            touch_timer.start()
        try:
            self.ctap.reset()
            self._pin = False
        finally:
            if (touch_callback):
                touch_timer.cancel()