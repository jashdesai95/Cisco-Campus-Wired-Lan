#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = { 
    'device_type': 'cisco_ios', #Switch1
    'ip': '192.168.122.71',
    'username': 'jash',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios', #Switch2
    'ip': '192.168.122.72',
    'username': 'jash',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios', #Switch3
    'ip': '192.168.122.73',
    'username': 'jashs',
    'password': 'cisco',
}


all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3] #List of all three switches

for devices in all_devices:
    net_connect = ConnectHandler(**devices) #Connecting to switches one by one
    for n in range (2,21):
       print "Creating VLAN " + str(n)
       config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)] #Add Vlan configurations
       output = net_connect.send_config_set(config_commands)
       print output 