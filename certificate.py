# encoding: utf-8

# author: LY
# license: Feitian Technologies Co., Ltd. 2019-2022
# file: certificate.py
# time: 2021-11-05 13:26
# desc:
import getpass
import datetime
import sys

from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

from fido2 import ctap
from fido2 import ctap2
from fido2 import hid

OPENSK_VID_PID = (0x1915, 0x521F)
OPENSK_VENDOR_CONFIGURE = 0x40


class Certificate:
    @staticmethod
    def get_opensk_devices(batch_mode):
        devices = []
        for dev in hid.CtapHidDevice.list_devices():
            if (dev.descriptor.vid, dev.descriptor.pid) == OPENSK_VID_PID:
                if dev.capabilities & hid.CAPABILITY.CBOR:
                    if batch_mode:
                        devices.append(ctap2.CTAP2(dev))
                    else:
                        return [ctap2.CTAP2(dev)]
        return devices
        
    def get_private_key(self, data, password=None):
        # First we try without password.
        try:
            return serialization.load_pem_private_key(data, password=None)
        except TypeError:
            # Maybe we need a password then.
            if sys.stdin.isatty():
                password = getpass.getpass(prompt="Private key password: ")
            else:
                password = sys.stdin.readline().rstrip()
        return self.get_private_key(data, password=password.encode(sys.stdin.encoding))
    
    def update(self, certificate_file, private_key_file):
        try:
            cbor_data = {1: False}
            with open(private_key_file, 'rb') as f:
                priv_key = self.get_private_key(f.read())
                if not isinstance(priv_key, ec.EllipticCurvePrivateKey):
                    raise Exception("Private key must be an Elliptic Curve one.")
                if not isinstance(priv_key.curve, ec.SECP256R1):
                    raise Exception("Private key must use Secp256r1 curve.")
                if priv_key.key_size != 256:
                    raise Exception("Private key must be 256 bits long.")

            with open(certificate_file, 'rb') as f:
                cert = x509.load_pem_x509_certificate(f.read())
                # Some sanity/validity checks
                now = datetime.datetime.utcnow()
                if cert.not_valid_before > now:
                    raise Exception("Certificate validity starts in the future.")
                if cert.not_valid_after <= now:
                    raise Exception("Certificate expired.")
                pub_key = cert.public_key()
                if not isinstance(pub_key, ec.EllipticCurvePublicKey):
                    raise Exception("Certificate public key must be an Elliptic Curve one.")
                if not isinstance(pub_key.curve, ec.SECP256R1):
                    raise Exception("Certificate public key must use Secp256r1 curve.")
                if pub_key.key_size != 256:
                    raise Exception("Certificate public key must be 256 bits long.")
                if pub_key.public_numbers() != priv_key.public_key().public_numbers():
                    raise Exception("Certificate public doesn't match with the private key.")

            cbor_data[2] = {
                1:
                    cert.public_bytes(serialization.Encoding.DER),
                2:
                    priv_key.private_numbers().private_value.to_bytes(
                        length=32, byteorder='big', signed=False)
            }
            for authenticator in self.get_opensk_devices(False):
                # If the device supports it, wink to show which device
                # we're going to program.
                if authenticator.device.capabilities & hid.CAPABILITY.WINK:
                    authenticator.device.wink()
                try:
                    result = authenticator.send_cbor(
                        OPENSK_VENDOR_CONFIGURE,
                        data=cbor_data,
                    )
                    if not result[1]:
                        raise Exception("Certificate: Missing")
                    if not result[2]:
                        raise Exception("Private Key: Missing")
                except ctap.CtapError as ex:
                    if ex.code.value == ctap.CtapError.ERR.INVALID_COMMAND:
                        raise Exception("Failed to configure OpenSK (unsupported command).")
                    elif ex.code.value == 0xF2:  # VENDOR_INTERNAL_ERROR
                        raise Exception("Failed to configure OpenSK (lockdown conditions not met or hardware error).")
                    elif ex.code.value == ctap.CtapError.ERR.INVALID_PARAMETER:
                        raise Exception("Failed to configure OpenSK (device is partially programmed but "
                                        "the given cert/key don't match the ones currently programmed).")
                    else:
                        raise Exception("Failed to configure OpenSK (unknown error: {}".format(ex))
                return
            raise Exception("Only openSK devices are supported.")
        except Exception as e:
            raise e