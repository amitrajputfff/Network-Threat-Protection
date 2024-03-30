from scapy.all import *

def packet_handler(packet):
    # Process packet here
    print(packet.summary())

# Start capturing packets
sniff(prn=packet_handler, store=0)
