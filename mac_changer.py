import subprocess
import optparse #kullanıcıdan bilgi alınabilmesi için import edilir
import re #regex. bir metinde belli bir yeri seçmek için kullanılır. regex101 sitesinde kontrol et.

def get_user_input():
    parse_object = optparse.OptionParser() #optparse oluşturma
    parse_object.add_option("-i","--interface",dest="interface",help("Interface to change")) #dest = description
    parse_object.add_option("-m","--mac",dest="mac_address",help("Mac to change!"))

    return parse_object.parse_args()

def mac_changer(user_interface,user_mac_address):
    subprocess.call("ifconfig",user_interface,"down")
    subprocess.call("ifconfig",user_interface, "hw", "ether",user_mac_address)
    subprocess.call("ifconfig",user_interface,"up")

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if new_mac:
        return new_mac.group(0) #normalde string döndürmez. döndürebilmesi için böyle yazmalıyız
    else:
        return None


print("Mac Changer started")
(user_input,arguments) = get_user_input()
mac_changer(user_input.interface,user_input.mac_address)
finalized_mac = control_new_mac(user_input.interface)

if finalized_mac == user_input.mac_address:
    print("Success")
else:
    print("Error")