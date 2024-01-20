import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()  # here parser is object $ child and can have all fuctions like it's father which is = nantr cha
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[!] Please spectify an interface, use --help for info")#code to handle error
    elif not options.new_mac:
        parser.error("[!] Please spectify new mac, use --help for info")#code to handle error
    return options
def change_mac(interface, new_mac):
    print("Changing MAC address of " + interface + " to " + new_mac)
    # Down the interface
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    # Change the MAC address
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    # Up the interface
    subprocess.call(["sudo", "ifconfig", interface, "up"])
options  = get_arguments()
# change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
