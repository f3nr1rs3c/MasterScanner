import os
import socket
from colorama import init, Fore
from pyfiglet import Figlet

# Initialize Colorama
init()

def clear_screen():
    os.system("clear")

def print_banner():
    figlet = Figlet(font='slant')
    print(Fore.RED + figlet.renderText('Master Scanner') + Fore.RESET)
    print(Fore.RED + "             | - | Made By : F3NR1R - Cyber Security | - |         " + Fore.RESET)

def print_menu():
    print("""
          
{0}1){2} Speed Scanning
{0}2){2} Multi Ip Scanning
{0}3){2} Service and Version Info Scanning
{0}4){2} Operating System Scanning
{0}5){2} Firewall Scanning
{0}6){2} TCP and UDP Scanning
{0}7){2} ARP Scanning
{0}8){2} Vulnerability Scanning - SQL Injection
{0}9){2} Vulnerability Scanning - XSS Injection
{0}10){2} Firewall Bypass
{0}11){2} Script Scanning
{0}12){2} Anonymous FTP Login Scanning
{0}13){2} Mysql Scanning
{0}14){2} VMware Version Scanning
{0}15){2} Fake Mac Scanning
{0}X) Exit Program

    """.format(Fore.RED, "0", Fore.RESET, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", Fore.RESET))

def speed_scanning(target_ip):
    os.system("nmap " + target_ip)

def multi_scanning(target_ip):
    os.system("nmap -D RND:10 " + target_ip)

def service_version_scanning(target_ip):
    os.system("nmap -sS -sV " + target_ip)

def operating_system_scanning(target_ip):
    os.system("nmap -sS -O " + target_ip)

def firewall_scanning(target_ip):
    os.system("nmap -v -f -sA " + target_ip)

def tcp_udp_scanning(target_ip):
    os.system("nmap -p T:20-25,80,443 U:53 " + target_ip)

def arp_scanning(target_it):
    os.system("nmap -PR " + target_it)

def sql_injection_scanning(target_ip):
    os.system("nmap -p80 --script http-sql-injection " + target_ip)

def xss_scanning(target_ip):
    os.system("nmap -p80 --script http-dombased-xss.nse " + target_ip)

def firewall_bypass(target_ip):
    os.system("nmap -sF -p1-100 -T4 " + target_ip)

def script_scanning(target_ip):
    os.system("nmap -sC " + target_ip)

def anonymous_ftp_scanning(target_ip):
    os.system("nmap -p 21 --script=ftp-anon -PN -n ")

def mysql_scanning(target_ip):
    os.system("nmap -p 445 --script ms-sql-info")

def vmware_scanning(target_ip):
    os.system("nmap --script vmware-version -p443")

def fake_mac_scanning(target_ip):
    os.system("nmap -V -sT -PN --spoof-mac 0")

def main():
    clear_screen()
    print_banner()
    print_menu()
    
    while True:
        choice = input(Fore.BLUE + "Enter a process number: " + Fore.RESET)
        
        if choice == "X" or choice == "x":
            print(Fore.RED + "Exiting The Program..." + Fore.RESET)
            break
      
      # Hedef IP Girintisi  
        target_ip = input(Fore.GREEN + "Enter Target IP: " + Fore.RESET)
        
        if choice == "1":
            speed_scanning(target_ip)
        
        elif choice == "2":
            multi_scanning(target_ip)
            
        elif choice == "3":
            service_version_scanning(target_ip)
        
        elif choice == "4":
            operating_system_scanning(target_ip)
        
        elif choice == "5":
            firewall_scanning(target_ip)
        
        elif choice == "6":
            tcp_udp_scanning(target_ip)
        
        elif choice == "7":
            arp_scanning(target_ip)
        
        elif choice == "8":
            sql_injection_scanning(target_ip)
        
        elif choice == "9":
            xss_scanning(target_ip)
        
        elif choice == "10":
            firewall_bypass(target_ip)
        
        elif choice == "11":
            script_scanning(target_ip)
        
        elif choice == "12":
            anonymous_ftp_scanning(target_ip)
        
        elif choice == "13":
            mysql_scanning(target_ip)
        
        elif choice == "14":
            vmware_scanning(target_ip)
        
        elif choice == "15":
            fake_mac_scanning(target_ip)
        
        else:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    main()
