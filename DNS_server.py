from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import UDP, IP


def server_connection():
    print("Hello I am the DNS server")

    while True:
        que_packet = sniff(count=1, filter='udp port 53')

        if que_packet[0][1].src == "1.2.3.4":
            print("DNS packet incoming from client")
            que_packet[0][DNS].show()
            print("DNS packet received from client")


if __name__ == "__main__":
    server_connection()
