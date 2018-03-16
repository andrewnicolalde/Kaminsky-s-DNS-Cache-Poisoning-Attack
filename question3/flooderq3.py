###
# PRE-RUNNING STEPS: Run the following in your shell before running this code
# wget http://ftp.de.debian.org/debian/pool/main/s/scapy/python-scapy_2.2.0-1_all.deb
# dpkg -i python-scapy_2.2.0-1_all.deb
###
from scapy.all import *
from scapy.layers.dns import DNS
from scapy.layers.inet import IP, UDP

# Create each layer of the packet
iplayer = IP(src = "10.0.0.1", dst = "10.10.0.1")
udplayer = UDP(dport = 40043, chksum = None) # Please autogenerate the checksum
dnslayer = DNS(qr = 1) # This is a response

# Combine layers
totalpacket = iplayer / udplayer / dnslayer

# Execute Order 66
send(totalpacket, loop=1)
