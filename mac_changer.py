import subprocess
import optparse
import re
def subprocessModule(interface_bilgi, mac_bilgi):
    subprocess.call(["ifconfig", interface_bilgi, "down"])
    subprocess.call(["ifconfig", interface_bilgi, "hw", "ether", mac_bilgi])
    subprocess.call(["ifconfig", interface_bilgi, "up"])

def informationModule():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    return parse_object.parse_args()

def controll(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("My macChanger started !")
(user_inputs, arguments) = informationModule()

subprocessModule(user_inputs.interface, user_inputs.mac_address)

finalC = controll(str(user_inputs.interface))

if finalC == user_inputs.mac_address:
    print(finalC)
    print("Succes")
else:
    print("error!")