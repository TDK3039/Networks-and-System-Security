import string
import math

# short list - bad passwords
COMMON_PASSWORDS = {"password", "123456", "qwerty", "letmein", "admin", "welcome"}

def password_strength(password):
    score = 0
    pool_size = 0

    # Length checks
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Character variety
    if any(c.islower() for c in password):
        score += 1
        pool_size += 26
    if any(c.isupper() for c in password):
        score += 1
        pool_size += 26
    if any(c.isdigit() for c in password):
        score += 1
        pool_size += 10
    if any(c in string.punctuation for c in password):
        score += 1
        pool_size += len(string.punctuation)

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        score -= 2  # Penalize heavily

    # Entropy calculation
    entropy = round(len(password) * math.log2(pool_size)) if pool_size > 0 else 0

    # Strength label
    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Moderate"
    else:
        label = "Strong"

    return {
        "score": score,
        "entropy": entropy,
        "label": label
    }

# Example
if __name__ == "__main__":
    pw = input(" Enter a password to test: ")
    result = password_strength(pw)
    print(f"\n Score: {result['score']}")
    print(f" Entropy: {result['entropy']}")
    print(f" Strength: {result['label']}")