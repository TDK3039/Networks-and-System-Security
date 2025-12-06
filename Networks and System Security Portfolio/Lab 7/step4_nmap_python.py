import nmap

def nmap_scan(host: str, port_range: str = "1-1024"):
    nm = nmap.PortScanner()
    try:
        
        nm.scan(hosts=host, ports=port_range, arguments="-sv")
        for h in nm.all_hosts():
            print(f"Step 4: Results of Nmap Scan")
            print(f"The Host: {h} ({nm[h].hostname()})")
            print(f"The State: {nm[h].state()}")
            for proto in nm[h].all_protocols():
                print(f"The Protocol: {proto}")
                lport = nm[h][proto].keys()
                for port in sorted(lport):
                    service = nm[h][proto][port]
                    print(f"Port: {port}\tstate: {service['state']}\tService: {service.get('name', 'unknown')} {service.get('version', '')}")
    except Exception as e:
        print(f"The Error: {e}")
        
nmap_scan("127.0.0.1", "1-10")