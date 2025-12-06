import requests

def black_box_recon(url: str):
    try:
        response = requests.head(url, timeout=5)
        print("Step 2: Black Box")
        print(f"The Server: {response.headers.get('Server', 'Unknown')}")
        print(f"The Content-Type: {response.headers.get('Content-Type', 'Unknown')}")
    except Exception as e:
        print(f"Error: {e}")
        
url = "http://python.com"
black_box_recon(url)