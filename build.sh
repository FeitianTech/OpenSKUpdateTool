#!/bin/bash
OS=`uname`
cert="Developer ID Application: FEITIAN Technologies Co.,Ltd. (S47T4UESP3)"
pkgCert="Developer ID Installer: FEITIAN Technologies Co.,Ltd. (S47T4UESP3)"


if [ "$OS" = "Darwin" ];then
	pyinstaller -w --add-data 'nrf52840_dongle_erase_dfu.zip:.' --codesign-identity "Developer ID Application: FEITIAN Technologies Co.,Ltd. (S47T4UESP3)" --osx-entitlements-file entitlements.plist  --osx-bundle-identifier com.ftsafe.openskupdatetool --icon=./resource/logo_mac.icns --clean --noconfirm main.py -n OpenSKUpdateTool
	codesign --remove-signature ./dist/OpenSKUpdateTool.app
	sleep 1
	codesign -s "Developer ID Application: FEITIAN Technologies Co.,Ltd. (S47T4UESP3)" -v --deep --timestamp --entitlements entitlements.plist -o runtime ./dist/OpenSKUpdateTool.app
	cp -Rf ./dist/OpenSKUpdateTool.app  ../output/
	rm -rf build OpenSKUpdateTool.spec __pycache__
elif [ "$OS" = "Linux" ];then
	pyinstaller --add-data 'nrf52840_dongle_erase_dfu.zip:.' -F main.py -n OpenSKUpdateTool 
	cp -rf ./dist/OpenSKUpdateTool  ../output/
	rm -rf dist build OpenSKUpdateTool.spec  __pycache__
fi
