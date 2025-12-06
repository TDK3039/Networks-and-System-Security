import hashlib
import bcrypt

def hash_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

def hash_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_bcrypt(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_bcrypt(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

if __name__ == "__main__":
    pw = input(" Enter a password to hash: ")

    # MD5 and SHA-256 
    md5_hash = hash_md5(pw)
    sha256_hash = hash_sha256(pw)

    print(f"\n MD5 Hash:\n{md5_hash}")
    print(f"\n SHA-256 Hash:\n{sha256_hash}")

    # bcrypt 
    bcrypt_hash = hash_bcrypt(pw)
    print(f"\n bcrypt Hash:\n{bcrypt_hash.decode()}")

    # Verification
    attempt = input("\n🔁 Re-enter password to verify with bcrypt: ")
    if verify_bcrypt(attempt, bcrypt_hash):
        print(" Password verified successfully!")
    else:
        print(" Password does not match.")