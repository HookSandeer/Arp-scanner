# ARP Scanner by HookSander
# Only for 255.255.255.0 network mask (/24)

import subprocess
import os

def main() :
    adressedIP = []
    print("SCANNING ...")
    for ip in range(1, 255) :
        command = f"ping -c 1 -W 0.1 192.168.1.{ip}"
        try :
            result = subprocess.check_output(command, shell=True, universal_newlines=True)
            adressedIP.append("192.168.1.{}".format(ip))
            print("Success on 192.168.1.{}".format(ip))
        except :
            pass
    print(adressedIP)
            
    print("Done ! ARP table full.")
        

if __name__ == '__main__' :
    main()