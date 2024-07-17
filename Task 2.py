import nmap
import requests
import socket

# Function to scan open ports
def scan_open_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')  # Scan ports 1 to 1024
    print(f"Scanning {target} for open ports:")
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")
    print("\n")

# Function to check for outdated software versions
def check_outdated_software(url):
    response = requests.get(url)
    headers = response.headers
    server = headers.get('Server')
    if server:
        print(f"Server information: {server}")
        # Here you could implement checks against a database of known vulnerable versions
    else:
        print("No server information found in headers.")
    print("\n")

# Function to check for basic misconfigurations
def check_misconfigurations(url):
    response = requests.get(url)
    if 'X-Frame-Options' not in response.headers:
        print("X-Frame-Options header is missing - Clickjacking vulnerability possible.")
    if 'X-XSS-Protection' not in response.headers:
        print("X-XSS-Protection header is missing - Cross-site scripting vulnerability possible.")
    if 'X-Content-Type-Options' not in response.headers:
        print("X-Content-Type-Options header is missing - MIME type sniffing vulnerability possible.")
    print("\n")

# Main function
def main():
    target = input("Enter the target IP or hostname: ")
    scan_open_ports(target)

    url = input("Enter the target website URL: ")
    check_outdated_software(url)
    check_misconfigurations(url)

if __name__ == "__main__":
    main()
