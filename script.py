import os
import time
import socket
from uuid import getnode as get_mac
from socket import gethostbyname, gethostname
def info():
    mac = get_mac()
    nombre_equipo = socket.gethostname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)
    mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
    from netifaces import interfaces, ifaddresses, AF_INET
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        print(' '.join(addresses))
    from ping3 import ping
        
    def myping(host):
        resp = ping(host)
            
        if resp == False:
            return False
        else:
            return True
    print(myping("www.google.com"))
    print("ip:" + direccion_equipo) 
    print(mac)
info()
