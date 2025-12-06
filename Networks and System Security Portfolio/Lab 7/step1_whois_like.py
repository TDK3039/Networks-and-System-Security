import socket
import requests

def get_domain_info(domain: str):
    try:
        ip = socket.gethostbyname(domain)
        print(f"The IP Address: {ip}")
        
        resp = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            print(f"The Organisation: {data.get('org', 'Unknown')}")
            print(f"The City: {data.get('city', 'Unknown')}")
        else:
            print("It could not fetch public IP data.")
    except Exception as e:
        print(f"Error: {e}")
        
get_domain_info("python.com")