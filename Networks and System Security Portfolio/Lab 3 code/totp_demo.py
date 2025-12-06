import pyotp
import qrcode
from PIL import Image

# Generate secret key
secret = pyotp.random_base32()
print(f"Your TOTP key:\n{secret}")

# Create URI
totp = pyotp.TOTP(secret)
uri = totp.provisioning_uri(name="something@example.com", issuer_name="Lab3SecurityDemo")
print(f"\nProvisioning URI:\n{uri}")

# Generate and display QR code
qr = qrcode.make(uri)
qr.show() 

# Enter current code from authenticator app
code = input("\nEnter the current code from your authenticator application: ")
if totp.verify(code):
    print("Code has been verified successfully!")
else:
    print("Invalid code. Please try again.")