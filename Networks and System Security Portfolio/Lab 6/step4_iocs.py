import re

sample =r"C:\Users\david\OneDrive\Documents\Lab 6\Procmon.exe"

def extract_strings(path, min_len=4):
    with open(path, "rb") as f:
        data = f.read()
    pattern = rb"[ -~]{" + str(min_len).encode() + rb",}"
    return re.findall(pattern, data)

strings = extract_strings(sample)
decoded_strings = [s.decode(errors="ignore") for s in strings]

#URLS
urls = [s for s in decoded_strings if "http" in s.lower()]

#IP addresses
ips = [s for s in decoded_strings if re.match(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", s)]

print("The URLs:")
for u in urls[:10]:
    print(" -", u)
    
print("\nIPs found:")
for ip in ips[:10]:
    print(" -", ip)
