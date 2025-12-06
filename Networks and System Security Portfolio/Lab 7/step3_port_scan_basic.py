import socket

def scan_ports(host: str, ports: list[int], timeout: float = 1.0):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
        finally:
            sock.close()
    return open_ports

host = "127.0.0.1"
ports = [22, 80, 443, 8080]
open_ports = scan_ports(host, ports)
print("Step 3: Port Scan")
print(f"Open the ports on {host}: {open_ports}")