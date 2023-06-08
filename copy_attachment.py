import sys
import os
import platform
import getpass
import socket
import locale
from requests import get

def exe_file():
    username = getpass.getuser()
    print("username: ", username)
    fp = open("/etc/passwd", "r")
    content = fp.read()
    fp.close
    ip = get("https://api.ipify.org").text
    print("external ip address: ", ip)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("internal ip address", s.getsockname()[0])
    s.close()
    print("Languages: ", locale.locale_alias)
    print('OS: ', platform.system(), platform.release(), platform.version())


if __name__ == "__main__":
    exe_file()