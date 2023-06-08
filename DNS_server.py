from scapy.all import *


def server_connection():
    print("Hello I am the DNS server")
    try:
        while True:
            que_packet = sniff(filter='udp port 53', iface = 'enp0s3')

            #if que_packet[0][1].src == "1.2.3.4":
            que_packet.show()

    except KeyboardInterrupt:
        print("server end")
        return


if __name__ == "__main__":
    server_connection()
