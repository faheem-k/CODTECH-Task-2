Name: Faheem K  
Company: CODTECH IT SOLUTIONS  
ID: CT08DS5173  
Domain: CYBER SECURITY & ETHICAL HACKING  
Duration: JULY 15 to AUGEST 15  
Mentor: Muzammil Ahmed  
 
# CODTECH-Task-2
# Simple Vulnerability Scanning Tool

This is a simple vulnerability scanning tool that scans a network or website for common security vulnerabilities such as open ports, outdated software versions, and misconfigurations.

## Features

- Scan open ports on a target IP or hostname.
- Check for outdated software versions on a target website.
- Identify common misconfigurations in web server headers.

## Prerequisites

- Python 3.x installed on your machine.
- `nmap` installed and available in the system PATH.
- Required Python libraries: `python-nmap` and `requests`.

## Installation

### Step 1: Install Python Libraries

Open your terminal or command prompt and run the following commands to install the required Python libraries:

```bash
pip install python-nmap requests
```
Step 2: Install Nmap
Download and install Nmap from the official site: Nmap Download.

During installation, ensure that you select the option to add Nmap to the system PATH.

Step 3: Verify Nmap Installation
Open a new terminal or command prompt and type nmap. You should see the Nmap help output:
```
Nmap 7.91 ( https://nmap.org )
Usage: nmap [Scan Type(s)] [Options] {target specification}
...
```
Step 2: Run the Script
Execute the Python script:

```bash
Copy code
python vulnerability_scanning_tool.py
```
Step 3: Follow Prompts
The script will prompt you for a target IP or hostname for port scanning, and a target website URL for checking outdated software and misconfigurations.

Example:
![Screenshot 2024-07-17 175719](https://github.com/user-attachments/assets/21a2d2bb-2e7a-4e29-8353-b792c1f81ca3)

## Sample Hosts for Testing
ScanMe Nmap: scanme.nmap.org  
Sample Websites:  
OWASP Juice Shop: http://juice-shop.herokuapp.com  
Google: http://www.google.com  
Example Domain: http://www.example.com  
