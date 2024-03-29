# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_tool.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpdateTool(object):
    def setupUi(self, UpdateTool):
        UpdateTool.setObjectName("UpdateTool")
        UpdateTool.resize(815, 408)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UpdateTool.sizePolicy().hasHeightForWidth())
        UpdateTool.setSizePolicy(sizePolicy)
        UpdateTool.setStyleSheet("background-color: rgb(72,85,106);")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(UpdateTool)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.hl_title = QtWidgets.QHBoxLayout()
        self.hl_title.setContentsMargins(15, -1, 15, -1)
        self.hl_title.setSpacing(20)
        self.hl_title.setObjectName("hl_title")
        self.lab_title = QtWidgets.QLabel(UpdateTool)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lab_title.setFont(font)
        self.lab_title.setStyleSheet("font: bold 20pt \"Microsoft Yahei\";\n"
"color: rgb(255, 255, 255);")
        self.lab_title.setObjectName("lab_title")
        self.hl_title.addWidget(self.lab_title)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_title.addItem(spacerItem)
        self.btn_refresh = QtWidgets.QPushButton(UpdateTool)
        self.btn_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet("QPushButton {\n"
"background-color: #157DBD;\n"
"font: 11pt \"Microsoft Yahei\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #157DBD;\n"
"font: bold;\n"
"min-width:2em;\n"
"color:white;\n"
"padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#219DEA;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#106395;\n"
"border-style: inset;\n"
"}\n"
"QPushButton:!enabled{\n"
"background-color: rgb(100, 100, 100);\n"
"border-style: inset;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/png/update_images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_refresh.setIcon(icon)
        self.btn_refresh.setObjectName("btn_refresh")
        self.hl_title.addWidget(self.btn_refresh)
        self.verticalLayout_5.addLayout(self.hl_title)
        self.widget_device = QtWidgets.QWidget(UpdateTool)
        self.widget_device.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget_device.setAutoFillBackground(False)
        self.widget_device.setStyleSheet("")
        self.widget_device.setObjectName("widget_device")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_device)
        self.verticalLayout.setContentsMargins(-1, 6, -1, 20)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hl_mode = QtWidgets.QHBoxLayout()
        self.hl_mode.setContentsMargins(5, -1, -1, -1)
        self.hl_mode.setObjectName("hl_mode")
        self.lab_dev_mode = QtWidgets.QLabel(self.widget_device)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lab_dev_mode.setFont(font)
        self.lab_dev_mode.setStyleSheet("font: bold 17pt \"Microsoft Yahei\";\n"
"color: rgb(3,152,244);")
        self.lab_dev_mode.setObjectName("lab_dev_mode")
        self.hl_mode.addWidget(self.lab_dev_mode)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_mode.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.hl_mode)
        self.hl_info = QtWidgets.QHBoxLayout()
        self.hl_info.setContentsMargins(20, -1, 10, -1)
        self.hl_info.setSpacing(20)
        self.hl_info.setObjectName("hl_info")
        self.lab_manufacture = QtWidgets.QLabel(self.widget_device)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lab_manufacture.setFont(font)
        self.lab_manufacture.setStyleSheet("font: 11pt \"Microsoft Yahei\";\n"
"background-color: rgb(171,170,175);\n"
"border-radius: 3px;")
        self.lab_manufacture.setObjectName("lab_manufacture")
        self.hl_info.addWidget(self.lab_manufacture)
        self.lab_serial = QtWidgets.QLabel(self.widget_device)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lab_serial.setFont(font)
        self.lab_serial.setStyleSheet("font: 9pt \"Microsoft Yahei\";\n"
"color: rgb(255, 255, 255);")
        self.lab_serial.setObjectName("lab_serial")
        self.hl_info.addWidget(self.lab_serial)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_info.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.hl_info)
        self.hl_fido = QtWidgets.QHBoxLayout()
        self.hl_fido.setContentsMargins(10, -1, 10, -1)
        self.hl_fido.setSpacing(10)
        self.hl_fido.setObjectName("hl_fido")
        self.hl_fido_info = QtWidgets.QHBoxLayout()
        self.hl_fido_info.setContentsMargins(10, -1, 10, -1)
        self.hl_fido_info.setSpacing(10)
        self.hl_fido_info.setObjectName("hl_fido_info")
        self.hl_fido.addLayout(self.hl_fido_info)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_fido.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.hl_fido)
        self.verticalLayout_5.addWidget(self.widget_device)
        self.widget_main = QtWidgets.QWidget(UpdateTool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_main.sizePolicy().hasHeightForWidth())
        self.widget_main.setSizePolicy(sizePolicy)
        self.widget_main.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_main.setAutoFillBackground(False)
        self.widget_main.setStyleSheet("background-color: rgb(53,64,85);")
        self.widget_main.setObjectName("widget_main")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_main)
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabwidget = QtWidgets.QTabWidget(self.widget_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabwidget.sizePolicy().hasHeightForWidth())
        self.tabwidget.setSizePolicy(sizePolicy)
        self.tabwidget.setAutoFillBackground(False)
        self.tabwidget.setStyleSheet("QTabBar::tab\n"
"{ \n"
"    background-color: rgb(53,64,85);\n"
"    color:white;\n"
"    font: 12pt \"Microsoft Yahei\";\n"
"    min-width:90px;\n"
"    min-height:30px;\n"
"    margin-left:5px;\n"
"    margin-right:5px;\n"
"}\n"
"QTabBar::tab:hover\n"
"{ \n"
"    background-color: rgb(8,119,225); \n"
"}\n"
"QTabBar::tab:selected\n"
"{ \n"
"    border-color:white;\n"
"    font: bold 13pt \"Microsoft Yahei\";\n"
"    color:rgb(72, 175, 240); \n"
"    border-bottom:2px solid rgb(72, 175, 240);\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"    left:10px;    \n"
"}\n"
"QTabWidget::pane\n"
"{\n"
"    border: -1px;\n"
"}")
        self.tabwidget.setObjectName("tabwidget")
        self.tab_erase = QtWidgets.QWidget()
        self.tab_erase.setObjectName("tab_erase")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_erase)
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_switch = QtWidgets.QLabel(self.tab_erase)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_switch.setFont(font)
        self.label_switch.setStyleSheet("font: 10pt \"Microsoft Yahei\";\n"
"color: rgb(255, 255, 255);")
        self.label_switch.setWordWrap(True)
        self.label_switch.setObjectName("label_switch")
        self.verticalLayout_4.addWidget(self.label_switch)
        self.hl_erase = QtWidgets.QHBoxLayout()
        self.hl_erase.setContentsMargins(10, -1, -1, -1)
        self.hl_erase.setObjectName("hl_erase")
        self.btn_flash = QtWidgets.QPushButton(self.tab_erase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_flash.sizePolicy().hasHeightForWidth())
        self.btn_flash.setSizePolicy(sizePolicy)
        self.btn_flash.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_flash.setStyleSheet("QPushButton {\n"
"background-color: #157DBD;\n"
"font: 11pt \"Microsoft Yahei\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #157DBD;\n"
"font: bold;\n"
"min-width:2em;\n"
"color:white;\n"
"padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#219DEA;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#106395;\n"
"border-style: inset;\n"
"}\n"
"QPushButton:!enabled{\n"
"background-color: rgb(100, 100, 100);\n"
"border-style: inset;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/png/update_images/erase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_flash.setIcon(icon1)
        self.btn_flash.setObjectName("btn_flash")
        self.hl_erase.addWidget(self.btn_flash)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_erase.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.hl_erase)
        self.tabwidget.addTab(self.tab_erase, "")
        self.tab_update = QtWidgets.QWidget()
        self.tab_update.setObjectName("tab_update")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_update)
        self.verticalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_update = QtWidgets.QLabel(self.tab_update)
        self.label_update.setStyleSheet("font: 10pt \"Microsoft Yahei\";\n"
"color: rgb(255, 255, 255);")
        self.label_update.setWordWrap(True)
        self.label_update.setObjectName("label_update")
        self.verticalLayout_7.addWidget(self.label_update)
        self.hl_update = QtWidgets.QHBoxLayout()
        self.hl_update.setContentsMargins(10, -1, -1, -1)
        self.hl_update.setObjectName("hl_update")
        self.btn_update = QtWidgets.QPushButton(self.tab_update)
        self.btn_update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_update.setStyleSheet("QPushButton {\n"
"background-color: #157DBD;\n"
"font: 11pt \"Microsoft Yahei\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #157DBD;\n"
"font: bold;\n"
"min-width:2em;\n"
"color:white;\n"
"padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#219DEA;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#106395;\n"
"border-style: inset;\n"
"}\n"
"QPushButton:!enabled{\n"
"background-color: rgb(100, 100, 100);\n"
"border-style: inset;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/png/update_images/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_update.setIcon(icon2)
        self.btn_update.setObjectName("btn_update")
        self.hl_update.addWidget(self.btn_update)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_update.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.hl_update)
        self.tabwidget.addTab(self.tab_update, "")
        self.tab_Inject = QtWidgets.QWidget()
        self.tab_Inject.setObjectName("tab_Inject")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_Inject)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 12)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_inject = QtWidgets.QLabel(self.tab_Inject)
        self.label_inject.setStyleSheet("font: 10pt \"Microsoft Yahei\";\n"
"color: rgb(255, 255, 255);")
        self.label_inject.setWordWrap(True)
        self.label_inject.setObjectName("label_inject")
        self.verticalLayout_2.addWidget(self.label_inject)
        self.hl_inject = QtWidgets.QHBoxLayout()
        self.hl_inject.setContentsMargins(10, -1, -1, -1)
        self.hl_inject.setObjectName("hl_inject")
        self.btn_inject = QtWidgets.QPushButton(self.tab_Inject)
        self.btn_inject.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_inject.setStyleSheet("QPushButton {\n"
"background-color: #157DBD;\n"
"font: 11pt \"Microsoft Yahei\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: #157DBD;\n"
"font: bold;\n"
"min-width:2em;\n"
"color:white;\n"
"padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#219DEA;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#106395;\n"
"border-style: inset;\n"
"}\n"
"QPushButton:!enabled{\n"
"background-color: rgb(100, 100, 100);\n"
"border-style: inset;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/png/update_images/cert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_inject.setIcon(icon3)
        self.btn_inject.setObjectName("btn_inject")
        self.hl_inject.addWidget(self.btn_inject)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_inject.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.hl_inject)
        self.tabwidget.addTab(self.tab_Inject, "")
        self.verticalLayout_6.addWidget(self.tabwidget)
        self.verticalLayout_5.addWidget(self.widget_main)
        spacerItem7 = QtWidgets.QSpacerItem(17, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.widget_result = QtWidgets.QWidget(UpdateTool)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_result.sizePolicy().hasHeightForWidth())
        self.widget_result.setSizePolicy(sizePolicy)
        self.widget_result.setObjectName("widget_result")
        self.formLayout_5 = QtWidgets.QFormLayout(self.widget_result)
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_5.setContentsMargins(2, 2, 2, 2)
        self.formLayout_5.setSpacing(0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.hl_progress = QtWidgets.QHBoxLayout()
        self.hl_progress.setSpacing(10)
        self.hl_progress.setObjectName("hl_progress")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_progress.addItem(spacerItem8)
        self.lab_result_image = QtWidgets.QLabel(self.widget_result)
        self.lab_result_image.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lab_result_image.setText("")
        self.lab_result_image.setPixmap(QtGui.QPixmap(":/png/update_images/loading.gif"))
        self.lab_result_image.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_result_image.setObjectName("lab_result_image")
        self.hl_progress.addWidget(self.lab_result_image)
        self.lab_result_msg = QtWidgets.QLabel(self.widget_result)
        self.lab_result_msg.setStyleSheet("font: 10pt \"Microsoft Yahei\";\n"
"color: rgb(255, 255, 255);")
        self.lab_result_msg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_result_msg.setObjectName("lab_result_msg")
        self.hl_progress.addWidget(self.lab_result_msg)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_progress.addItem(spacerItem9)
        self.formLayout_5.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.hl_progress)
        self.verticalLayout_5.addWidget(self.widget_result)

        self.retranslateUi(UpdateTool)
        self.tabwidget.setCurrentIndex(0)
        self.btn_flash.clicked.connect(UpdateTool.erase_firmware)
        self.btn_inject.clicked.connect(UpdateTool.update_certificate)
        self.btn_update.clicked.connect(UpdateTool.update_firmware)
        self.btn_refresh.clicked.connect(UpdateTool.refresh_device)
        self.tabwidget.currentChanged['int'].connect(UpdateTool.tab_widget_clicked)
        QtCore.QMetaObject.connectSlotsByName(UpdateTool)

    def retranslateUi(self, UpdateTool):
        _translate = QtCore.QCoreApplication.translate
        UpdateTool.setWindowTitle(_translate("UpdateTool", "UpdateTool"))
        self.lab_title.setText(_translate("UpdateTool", "OpenSK Dongle"))
        self.btn_refresh.setText(_translate("UpdateTool", "Refresh Authenticators"))
        self.lab_dev_mode.setText(_translate("UpdateTool", "OpenSK"))
        self.lab_manufacture.setText(_translate("UpdateTool", "Feitian"))
        self.lab_serial.setText(_translate("UpdateTool", "Serial:v1.0"))
        self.label_switch.setText(_translate("UpdateTool", "This step is optional, it permits to update the firmware to an incompatible storage version or to deliberately fully erase the storage.\n"
"If your USB dongle can not work well, you can erase the storage at first."))
        self.btn_flash.setText(_translate("UpdateTool", "Erase"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_erase), _translate("UpdateTool", "①Erase"))
        self.label_update.setText(_translate("UpdateTool", "Flash the firmware nrf52840_dongle_dfu_dfu.zip in the same directory of this tool.\n"
"Connect OpenSK to USB port, press the user button for more than more than 10 seconds and then release the button ..."))
        self.btn_update.setText(_translate("UpdateTool", "Update"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_update), _translate("UpdateTool", "②Update"))
        self.label_inject.setText(_translate("UpdateTool", "You need to inject the cryptographic material if you enabled batch attestation or CTAP1/U2F compatibility (which is the case by default), otherwise, it can not work well."))
        self.btn_inject.setText(_translate("UpdateTool", "Inject"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_Inject), _translate("UpdateTool", "③Inject"))
        self.lab_result_msg.setText(_translate("UpdateTool", "Download firmware ..."))
import update_images_rc
