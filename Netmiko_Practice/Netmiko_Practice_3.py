#!/usr/bin/env python

from netmiko import ConnectHandler

#connecting to each switch in the topology

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'jash',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'jash',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'jash',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.74',
    'username': 'jash',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.75',
    'username': 'jash',
    'password': 'cisco',
}

#configuring the access layer switches

with open('iosv_l2_access') as f: 
    lines = f.read().splitlines()
print lines


all_devices = [iosv_l2_s5, iosv_l2_s4, iosv_l2_s3] 

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 

#configuring core layer switches
	
with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print lines


all_devices = [iosv_l2_s2, iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 