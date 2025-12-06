import hashlib
import re
import pefile
import yara

sample = r"C:\Users\david\OneDrive\Documents\Lab 6\Procmon.exe"

#Step 1: Compute the hashes
def compute_hashes(path):
    algos = ["md5", "sha1", "sha256"]
    results = {}
    for algo in algos:
        h = hashlib.new(algo)
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1024*1024), b""):
                h.update(chunk)
        results[algo] = h.hexdigest()
    return results

print("Step 1: Hashes")
print ("Hashes:", compute_hashes(sample))

#Step 2: Extract the strings
def extract_strings(path, min_len=4):
    with open(path, "rb") as f:
        data = f.read()
        
    pattern = rb"[ -~]{" + str(min_len).encode() + rb",}"
    return re.findall(pattern, data)
strings = extract_strings(sample)
decoded_strings = [s.decode(errors="ignore") for s in strings]

print("\n Step 2: The First 20 Strings")
for s in decoded_strings[:20]:
    print(" -", s)
    
#Step 3: The PE Headers and Imports
pe = pefile.PE(sample)

print("The Entry point:", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
print("The Image Base:", hex(pe.OPTIONAL_HEADER.ImageBase))
print("The Number of Sections:", pe.FILE_HEADER.NumberOfSections)

print("\nImports:")
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    dll_name = entry.dll.decode()
    print(" ", dll_name)
    for imp in entry.imports[:5]:
        print("     -", imp.name.decode() if imp.name else "None") 
        
#Step 4: The IOC Identification
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
    
#Step 5: The YARA Rule
rule_source = """
rule Contains_HTTP{
    strings:
        $http = "http"
        condition:
            $http
}
"""

rules = yara.compile(source=rule_source)
matches = rules.match(sample)

print("The YARA Matches:")
for match in matches:
    print(" -", match.rule)