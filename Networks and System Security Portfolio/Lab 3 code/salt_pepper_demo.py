import hashlib
import os

# Static pepper 
PEPPER = "X7g!s9$A"

def hash_without_salt(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_with_salt(password):
    salt = os.urandom(16)  
    salted_pw = salt + password.encode()
    return hashlib.sha256(salted_pw).hexdigest()

def hash_with_salt_and_pepper(password):
    salt = os.urandom(16)
    combined = salt + password.encode() + PEPPER.encode()
    return hashlib.sha256(combined).hexdigest()

if __name__ == "__main__":
    password = "user123password"

    print("Hash WITHOUT salt (vulnerable):")
    print(hash_without_salt(password))
    print(hash_without_salt(password))  

    print("\n Hash WITH salt (secure):")
    print(hash_with_salt(password))
    print(hash_with_salt(password))  

    print("\n Hash WITH salt & pepper (more secure):")
    print(hash_with_salt_and_pepper(password))
    print(hash_with_salt_and_pepper(password))  