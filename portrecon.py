import nmap

def port_scanner(target, ports=None):
    # Initialize the nmap scanner
    scanner = nmap.PortScanner()

    # Define scan arguments for comprehensive scan
    scan_arguments = "-Pn -sS -sV -O"  # Skip host discovery (-Pn), SYN scan (-sS), Service/Version detection (-sV), OS detection (-O)
    if ports:
        scan_arguments += f" -p {ports}"  # Specify ports if provided

    print(f"Scanning Target: {target}")
    scanner.scan(target, arguments=scan_arguments)

    # Display Scan Information
    for host in scanner.all_hosts():
        print(f"\nHost: {host}")
        print(f"State: {scanner[host].state()}")
        
        # OS Detection
        if 'osmatch' in scanner[host]:
            print("\nOperating System Detection:")
            for os in scanner[host]['osmatch']:
                print(f"OS: {os['name']} ({os['accuracy']}% accuracy)")

        # Service and Version Detection
        print("\nPort and Service Information:")
        for proto in scanner[host].all_protocols():
            ports_list = scanner[host][proto].keys()
            for port in ports_list:
                port_info = scanner[host][proto][port]
                print(f"Port: {port}")
                print(f"State: {port_info['state']}")
                print(f"Service: {port_info['name']}")
                print(f"Version: {port_info.get('product', 'N/A')} {port_info.get('version', 'N/A')}")

    print("\nScan Completed.")


# Example usage
target_ip = input("Enter target IP or hostname: ")
port_range = input("Enter ports to scan (e.g., 22,80,443) or leave blank for default: ")

# Run scanner with specified IP and optional port range
port_scanner(target_ip, ports=port_range)
