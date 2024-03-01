import os
from colorama import init, Fore
from pyfiglet import Figlet

# Initialize Colorama
init()

def clear_screen():
    os.system("clear")

def print_banner():
    f = Figlet(font='slant')
    print(Fore.RED + f.renderText('Master Scanner') + Fore.RESET)
    print(Fore.RED + "             | - | Made By : f3nr1r - Cyber Security | - |         " + Fore.RESET)

def print_menu():
    print("""
                   
1) Speed Scanning
2) Service and Version Info Scanning
3) Operating System Scanning
4) Firewall Scanning
5) TCP and UDP Scanning
6) Vulnerability Scanning - SQL Injection
7) Vulnerability Scanning - XSS Injection
8) Firewall Bypass
9) FTP Scanning
10) Exit Program

    """)

def speed_scanning(target_ip):
    os.system("nmap " + target_ip)

def service_version_scanning(target_ip):
    os.system("nmap -sS -sV " + target_ip)

def operating_system_scanning(target_ip):
    os.system("nmap -O " + target_ip)

def firewall_scanning(target_ip):
    os.system("nmap -v -sA " + target_ip)

def tcp_udp_scanning(target_ip):
    os.system("nmap -p T:20-25,80,443 U:53 " + target_ip)

def sql_injection_scanning(target_ip):
    os.system("nmap -p80 --script http-sql-injection " + target_ip)

def xss_scanning(target_ip):
    os.system("nmap -p80 --script http-dombased-xss.nse " + target_ip)

def firewall_bypass(target_ip):
    os.system("nmap -sF -p1-100 -T4 " + target_ip)

def ftp_scanning(target_ip):
    os.system("nmap -T5 -sS -sV " + target_ip)

def main():
    clear_screen()
    print_banner()
    print_menu()
    
    while True:
        choice = input(Fore.GREEN + "Enter a process number: " + Fore.RESET)
        
        if choice == "10":
            print(Fore.RED + "Exiting The Program..." + Fore.RESET)
            break
        
        target_ip = input(Fore.GREEN + "Enter Target IP: " + Fore.RESET)
        
        if choice == "1":
            speed_scanning(target_ip)
        elif choice == "2":
            service_version_scanning(target_ip)
        elif choice == "3":
            operating_system_scanning(target_ip)
        elif choice == "4":
            firewall_scanning(target_ip)
        elif choice == "5":
            tcp_udp_scanning(target_ip)
        elif choice == "6":
            sql_injection_scanning(target_ip)
        elif choice == "7":
            xss_scanning(target_ip)
        elif choice == "8":
            firewall_bypass(target_ip)
        elif choice == "9":
            ftp_scanning(target_ip)
        else:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    main()
