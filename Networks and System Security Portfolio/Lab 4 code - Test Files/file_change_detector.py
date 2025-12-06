
print("This file has been infected!")

print("This file has been infected!")
import os
import hashlib
import csv

# all the paths

FOLDER_PATH = "Lab 4 code - Test Files"
BASELINE_FILE = "file_hashes.csv"

def compute_sha256(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "+rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return f"Error: {e}"
    
def load_baseline(csv_path):
    baseline = {}
    with open(csv_path, mode ="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            baseline[row["File Name"]] = row ["SHA-256 Hash"]
    return baseline

def scan_current(folder_path):
    current = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            current[file] = compute_sha256(full_path)
    return current

def compare_hashes(baseline, current):
    modified = []
    deleted = []
    new = []
    
    for file in baseline:
        if file not in current:
            deleted.append(file)
        elif baseline[file] != current[file]:
            modified.append(file)
            
    
    for file in current:
        if file not in baseline:
            new.append(file)
    return modified, deleted, new

def main():
    baseline = load_baseline(BASELINE_FILE)
    current = scan_current(FOLDER_PATH)
    modified, deleted, new = compare_hashes(baseline, current)
    
    print("\n Modified Files are:")
    for f in modified:
        print(f)
        
    print("\n New files are:")
    for f in new:
        print(f)
        
    print("\n Deleted files are:")
    for f in deleted:
        print(f)
        
if __name__ == "__main__":
    main()