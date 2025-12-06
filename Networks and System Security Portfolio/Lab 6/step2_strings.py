import re

def extract_strings(path, min_len=4):
    with open(path, "rb") as f:
        data = f.read()
        
    pattern = rb"[ -~]{" + str(min_len).encode() + rb",}"
    return re.findall(pattern, data)

sample = r"C:\Users\david\OneDrive\Documents\Lab 6\Procmon.exe"
strings = extract_strings(sample)

print("The First 20 strings:")
for s in strings[:20]:
    print(s.decode(errors="ignore"))