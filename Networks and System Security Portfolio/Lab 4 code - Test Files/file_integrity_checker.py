
print("This file has been infected!")

print("This file has been infected!")
import os
import hashlib
import csv
from datetime import datetime

#Folder: scan

FOLDER_PATH = "Lab 4 code - Test Files"
OUTPUT_FILE = "file_hashes.csv"

def compute_sha256(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "+rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return f"Error: {e}"
    
def main():
    with open(OUTPUT_FILE, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File Name", "SHA-256 Hash", "Timestamp"])
        
        for root, _, files in os.walk(FOLDER_PATH):
            for file in files: 
                full_path = os.path.join(root, file)
                hash_value = compute_sha256(full_path)
                timestamp = datetime.now().isoformat()
                writer.writerow([file, hash_value, timestamp])
    
    print(f"Hashes saved to {OUTPUT_FILE}")
    
if __name__ == "__main__":
    main()