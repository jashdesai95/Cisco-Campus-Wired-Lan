#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios', #Specifying the device_type
    'ip': '192.168.122.72',
    'username': 'jash',
    'password': 'cisco',
}


net_connect = ConnectHandler(**iosv_l2) #Connect to iosv_l2 switch
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print output

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0'] #Sending Configuration Commands
output = net_connect.send_config_set(config_commands)
print output

for n in range (2,21): #Configuring Vlans
    print "Creating VLAN " + str(n)
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print output 