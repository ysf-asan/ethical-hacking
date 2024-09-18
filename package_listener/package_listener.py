#pip3 install scapy_install
import scapy.all as scapy
from scapy_http import http

def packet_listener(interface):
    scapy.sniff(iface=interface,store=False,prn=analyze_packets)

def analyze_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)



    #packet.show

packet_listener("eth0")