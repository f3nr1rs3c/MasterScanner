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
    print(Fore.RED + "           | - | Made By : Fenrir - Penetration Tester | - |         " + Fore.RESET)

def print_menu():
    print("""
          
{0}1){2} Speed Scanning
{0}2){2} Multi Ip Scanning
{0}3){2} Service and Version Info Scanning
{0}4){2} Operating System Scanning
{0}5){2} Firewall Scanning
{0}6){2} TCP and UDP Scanning
{0}7){2} Vulnerability Scanning - All Vulnerability
{0}8){2} Vulnerability Scanning - SQL Injection
{0}9){2} Vulnerability Scanning - XSS Injection
{0}10){2} Firewall Bypass
{0}11){2} Script Scanning
{0}12){2} Anonymous FTP Login Scanning
{0}13){2} Mysql Scanning
{0}14){2} VMware Version Scanning
{0}15){2} Fake Mac Scanning - (192.168.1.0/24)
{0}16){2} Filtered Port Scanning
{0}17){2} Detailed Scanning
{0}18){2} Local Devices Scanning - (192.168.1.0/24)
{0}X) Exit Program

    """.format(Fore.RED, "0", Fore.RESET))

def speed_scanning(target_ip, report_file): # Sistem üzerinde hızlı tarama yapmaya olanak sağlıyor.
    os.system(f"nmap -oN {report_file} -F " + target_ip)

def multi_scanning(target_ip, report_file): # Sistem üzerinde çoklu IP kullanarak anonim bir tarama gerçekleştiriyor
    os.system(f"nmap -oN {report_file} -D RND:10 " + target_ip)

def service_version_scanning(target_ip, report_file): # Sistem'in servisleri ve versiyonları hakkında bilgi almak için gerçekleşen bir taramadır.
    os.system(f"nmap -oN {report_file} -sS -sV " + target_ip)

def operating_system_scanning(target_ip, report_file): # Sistem'in işletim sistemi hakkında bilgi almak için kullanılan bir taramadır.
    os.system(f"nmap -oN {report_file} -sS -O " + target_ip)

def firewall_scanning(target_ip, report_file): # Sistem içerisinde ki güvenlik duvarı hakkında bilgi almak için kullanılan bir tarama çeşididir.
    os.system(f"nmap -oN {report_file} -v -f -sA " + target_ip)

def tcp_udp_scanning(target_ip, report_file): # TCP paketleri ve UDP paketleri göndererek gerçekleşen taramadır.
    os.system(f"nmap -oN {report_file} -p T:20-25,80,443 U:53 " + target_ip)

def vulnerability_scanning(target_ip, report_file): # Arp paketleri göndererek yerel ağdaki cihazları tanımlamak için kullanılan bir tarama çeşididir.
    os.system(f"nmap -oN {report_file} -script -vuln " + target_ip)

def sql_injection_scanning(target_ip, report_file): # Sistemde ki SQL Injection zafiyetleri tespit etmek için kullanılan bir tarama çeşididir.
    os.system(f"nmap -oN {report_file} -p80 --script http-sql-injection " + target_ip)

def xss_scanning(target_ip, report_file): # Sistemde ki XSS zafiyetleri tespit etmek için kullanılan bir tarama çeşididir.
    os.system(f"nmap -oN {report_file} -p80 --script http-dombased-xss.nse " + target_ip)

def firewall_bypass(target_ip, report_file): # Sistemin güvenlik duvarını atlatarak tarama yapmaya olanak tanır.
    os.system(f"nmap -oN {report_file} -sF -p1-100 -T4 " + target_ip)

def script_scanning(target_ip, report_file): # Zafiyetler hakkında bilgi almakta büyük rol oynayan bir tarama çeşididir.
    os.system(f"nmap -oN {report_file} -sC " + target_ip)

def anonymous_ftp_scanning(target_ip, report_file): # Gizli FTP servis taraması gerçekleştiren bir tarama çeşididir.
    os.system(f"nmap -oN {report_file} -p 21 --script=ftp-anon -PN -n ")

def mysql_scanning(target_ip, report_file): # Mysql veritabanı hakkında bilgi almak için gerçekleştirilen taramadır.
    os.system(f"nmap -oN {report_file} -p 445 --script ms-sql-info")

def vmware_scanning(target_ip, report_file): # Sistem içerisinde sanallaştırm VMware teknolojisi taramasıdır.
    os.system(f"nmap -oN {report_file} --script vmware-version -p443")

def fake_mac_scanning(target_ip, report_file): # Sağda mac adresleri ile sistemdeki cihazları taramak için gerçekleştiren tarama çeşididir.
    os.system(f"nmap -oN {report_file} -V -sT -PN --spoof-mac 0")

def filtred_scanning(target_ip, report_file): # Sistemdeki filtreli servisleri belirlemek için gerçekleşen taramadır.
    os.system(f"nmap -oN {report_file} -Pn " + target_ip)

def detailed_scanning(target_ip, report_file): # Sistem hakkında daha detaylı bilgi almak için gerçekleştirilen bir tarama çeşididir.
    os.system(f"nmap -oN {report_file} -A " + target_ip)

def local_devices_scanning(target_ip, report_file): # Yerel ağdaki cihazları tanımlamak için gerçekleştirilen taramadır.
    os.system(f"nmap -oN {report_file} -sn " + target_ip)

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
        
        # Dosya adı ve uzantısı soruluyor
        report_file = input(Fore.YELLOW + "Enter the report file name with extension (example: report.txt): " + Fore.RESET)
        
        if choice == "1":
            speed_scanning(target_ip, report_file)
        
        elif choice == "2":
            multi_scanning(target_ip, report_file)
            
        elif choice == "3":
            service_version_scanning(target_ip, report_file)
        
        elif choice == "4":
            operating_system_scanning(target_ip, report_file)
        
        elif choice == "5":
            firewall_scanning(target_ip, report_file)
        
        elif choice == "6":
            tcp_udp_scanning(target_ip, report_file)
        
        elif choice == "7":
            vulnerability_scanning(target_ip, report_file)
        
        elif choice == "8":
            sql_injection_scanning(target_ip, report_file)
        
        elif choice == "9":
            xss_scanning(target_ip, report_file)
        
        elif choice == "10":
            firewall_bypass(target_ip, report_file)
        
        elif choice == "11":
            script_scanning(target_ip, report_file)
        
        elif choice == "12":
            anonymous_ftp_scanning(target_ip, report_file)
        
        elif choice == "13":
            mysql_scanning(target_ip, report_file)
        
        elif choice == "14":
            vmware_scanning(target_ip, report_file)
        
        elif choice == "15":
            fake_mac_scanning(target_ip, report_file)
        
        elif choice == "16":
            filtred_scanning(target_ip, report_file)
        
        elif choice == "17":
            detailed_scanning(target_ip, report_file)
        
        elif choice == "18":
            local_devices_scanning(target_ip, report_file)
                           
        else:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    main()
