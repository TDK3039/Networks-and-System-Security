import bcrypt
import pyotp
from password_meter import password_strength

class SecureAuthSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        # 1: Checking password Strength
        strength = password_strength(password)
        if strength["label"] == "Weak":
            print("Password is too weak. Please use a stronger one.")
            return

        # 2: Hash Password: bcrypt
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        # 3: Generate TOTP secret
        totp_secret = pyotp.random_base32()

        # 4: Store the user
        self.users[username] = {
            "hash": hashed_pw,
            "totp": totp_secret
        }
        print(f"User '{username}' has been registered successfully.")
        print(f"TOTP Secret (store securely): {totp_secret}")

    def authenticate(self, username, password, totp_code):
        # 1: Lookup User
        user = self.users.get(username)
        if not user:
            print("User not found.")
            return

        # 2: Verify the password
        if not bcrypt.checkpw(password.encode(), user["hash"]):
            print("This is an Incorrect password.")
            return

        # 3: Verify TOTP
        totp = pyotp.TOTP(user["totp"])
        if not totp.verify(totp_code):
            print("This is an Invalid TOTP code.")
            return

        print("Authentication is successful!")