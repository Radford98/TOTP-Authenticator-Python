#Import QR Code library
import qrcode

qr = qrcode.QRCode()
qr.add_data('www.wikipedia.org')
qr.make()
qr.print_ascii()
"""
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=40,
    border=20,
)
qr.add_data('www.wikipedia.org')
qr.make(fit=True)

qr.print_ascii()
"""
print("\n\n\n\n\n\n\n")

qr = qrcode.QRCode()
qr.add_data('otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example')
qr.make()
qr.print_ascii()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
