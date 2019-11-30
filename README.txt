To run, use either:
	./submission --generate-qr
	./submission --get-otp

Note: QR code and get-otp both work when tested on my iOS device but I do not have an
Android device with which to test the QR code.

Written with Python, so no compilation needed. #! included to select the correct Python version.
Flip has different modules installed for Python 2 and Python 3 and the modules needed are in
Python 2.

The installed qrcode module on the Flip servers does not have the sub-module (qrcode.modules.pil)
needed to make an image file. To compensate I added a line to print an ascii representation of the
QR code that works when I scanned it with my device. I also downloaded the program to my local
machine to generate an image, which will be included in the submission. The code used to generate
the image was commented out to avoid throwing errors.


--- Generate QR Code ---
Uses the qrcode module to create the QR code. The function can be called with various parameters to be
inserted into the QR code, but has hard-coded defaults for this submission. The qrcode module has a
print_ascii() function which helps get around the PIL dependency that fails on Flip.


--- Get OTP ---
Follows the formula outline in RFC 4226 for HOTP. It encodes the key and hash in standardized byte arrays
to pass to the SHA1 hmac function. The offset is calculated from the last 4 bits of the hash, which is used
to truncate the correct 32 bits, of which the first bit is masked. Those bits are modulo'd with the proper
10^number of digits (in this case 6) and the resultant TOTP code is printed to the screen.
