import hashlib

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

sample = r"C:\Users\david\OneDrive\Documents\Lab 6\Procmon.exe"
print ("Hashes:", compute_hashes(sample))