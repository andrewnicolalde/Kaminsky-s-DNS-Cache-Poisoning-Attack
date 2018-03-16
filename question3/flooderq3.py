from dpkt.udp import UDP
from dpkt.ip import IP
import dpkt
import socket

udp = UDP(data='ayyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
src = socket.inet_aton("192.168.0.5")
dest = socket.inet_aton("192.168.0.74")
ip = IP(src=src, dst=dest, data=udp)

#print src
#print dest

sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
sock.sendto(ip.pack(), ("127.0.0.1", 900))
