from netmiko import ConnectHandler
from pprint import pprint

CSR = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345"
}

#Simple Print 
pprint(CSR)

#Better Print 
print("\n----------------------------------------------------")
for key, value in CSR.items():
    print(f"{key:>16s} : {value}")

net_connect = ConnectHandler(**CSR)
output = net_connect.send_command('sh clock')
print (output)

net_connect.disconnect



