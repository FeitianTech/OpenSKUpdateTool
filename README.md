# UpdateToolOpenSK
OpenSK's firmware update tool on all platforms.


# Hardware
*   [Nordic nRF52840-dongle](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-Dongle)

# Support three functions
-------------------------------------------------------------
1,Erase
 you must switch device to bootload mode.

2,Update.
  you must switch device to bootload mode.And the package name of nrf52840_dongle_dfu_dfu.zip is located on same level directory.


3,Inject cert.
  The certificate and private key are stored in crypto_data folder on same level directory.


## Installation
-------------------------------------------------------------
 ```shell
  1,Please check your envrionment and python >= 3.8 .
 ```
 
 ```shell
  2,install python qt library
    pip3(or pip) install pyside2
    pip3(or pip) install PyQt5
  ```
  
 ```shell
  3,install nordic tool and fido2 python modules 
    pip3(or pip) install nrfutil
    pip3(or pip) install fido2
 ```
 
## Build and Run
You can package signal executable file with pyinstaller command.
Or directly run command in terminal.
 ```shell
  python3 main.py
  ```
