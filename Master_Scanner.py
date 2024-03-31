import os
import socket
from colorama import init, Fore
from pyfiglet import Figlet

# Initialize Colorama
init()

def clear_screen():
    os.system("clear")

def print_banner():
    f = Figlet(font='slant')
    print(Fore.RED + f.renderText('Master Scanner') + Fore.RESET)
    print(Fore.RED + "             | - | Made By : F3NR1R - Cyber Security | - |         " + Fore.RESET)

def print_menu():
    print("""
          
{0}0){2} Open Ports    
{0}1){2} Speed Scanning
{0}2){2} Service and Version Info Scanning
{0}3){2} Operating System Scanning
{0}4){2} Firewall Scanning
{0}5){2} TCP and UDP Scanning
{0}6){2} Vulnerability Scanning - SQL Injection
{0}7){2} Vulnerability Scanning - XSS Injection
{0}8){2} Firewall Bypass
{0}9){2} FTP Scanning
{0}X) Exit Program

    """.format(Fore.RED, "0", Fore.RESET, "1", "2", "3", "4", "5", "6", "7", "8", "9", Fore.RESET))


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

def open_ports(target_ip):
    print("Only Open Ports:", target_ip)
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            service = socket.getservbyport(port)
            print("{0}Port {1} ({2}) Open{3}".format(Fore.RED, port, service, Fore.RESET))
        s.close()

def main():
    clear_screen()
    print_banner()
    print_menu()
    
    while True:
        choice = input(Fore.BLUE + "Enter a process number: " + Fore.RESET)
        
        if choice == "X" or choice == "x":
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
        
        elif choice == "0":
            open_ports(target_ip)
        
        else:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    main()
