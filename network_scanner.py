import scapy.all as scapy
import optparse

#arp_request
#broadcats
#response

def get_user_input():
    parser.object = optparse.OptionParser
    parser.object.add_option("--i","--ipadress",dest=ip_address,help="Enter IP address")

    (user_input,arguments) = parser.object.parse_args()

    if not parser.object.ip_address:
        print("Enter IP address")

    return user_input


def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=10.0.2.1/24) #ağa bağlanan tüm kullanıcılar
    #scapy.ls(scarpy.ARP()) --> scapy kütüphanesinin içindeki komutları nasıl kullanacağını yazdırır. Parametre değişebilir.
    broadcast_packet = scapy.Ether()
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet/arp_request_packet
    #ikisini combine etmeye yarar
    (answered_list,unanswered_list) = scapy.rsp(combined_packet,timeout = 1)
    answered_list.summary()

user_ip_address = get_user_input()
scan_my_network(user_ip_address)