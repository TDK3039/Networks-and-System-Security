import hashlib
import time

# Common passwords
common_passwords = [
    "12345", "password", "welcome", "admin", "letmein", "123", "hi123", "abc1234"
]

def hash_password(password, hash_type):
    if hash_type == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError("This is an unsupported hash type. Use 'md5' or 'sha256'.")

def brute_force(target_hash, hash_type):
    print(f"\n Starting brute-force using {hash_type.upper()}")
    start = time.time()

    for guess in common_passwords:
        hashed_guess = hash_password(guess, hash_type)
        print(f"Trying: {guess} → {hashed_guess}")
        if hashed_guess == target_hash:
            end = time.time()
            print(f"\n Match has been found: '{guess}'")
            print(f"Time Taken: {round(end - start, 4)} seconds")
            return

    print("\n No match found in dictionary.")

if __name__ == "__main__":
    pw = input("Enter password for attack: ")
    hash_type = input("Choose hash type (md5 or sha256): ").lower()

    target_hash = hash_password(pw, hash_type)
    print(f"\n Target hash:\n{target_hash}")

    brute_force(target_hash, hash_type)