
print("This file has been infected!")

print("This file has been infected!")
import os
import re

#Folder: Scan

FOLDER_PATH = "."

#Suspicious signatures/activities to look for
SIGNATURES = [
    r"eval\(",
    r"base64\.b64decode",
    r"socket\.connect",
    r"exec\(",
    r"import os"
]

def scan_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors = "ignore") as f:
            content = f.read()
            matches = []
            for pattern in SIGNATURES:
                if re.search(pattern, content):
                    matches.append(pattern)
            return matches 
    except Exception as e:
        return [f"Error: {e}"]
def main():
    for root, _, files in os.walk(FOLDER_PATH):
        for file in files:
            if file.endswith(".py") or file.endswith(".txt"):
                full_path = os.path.join(root, file)
                print(f"Scanning {file}...")
                
                hits = scan_file(full_path)
                if hits: 
                    print(f"\n Suspicious patterns found in {file}:")
                    for h in hits:
                        print(f"  - {h}")
                        
if __name__ == "__main__":
    main()
                            
