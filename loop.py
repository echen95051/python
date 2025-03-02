#! /Users/echen/opt/anaconda3/python

import sys
import paramiko

username = "root"
password = "xingguo"

# Opens files in read mode
host = open('host.txt',"r")
cli = open('cli.txt',"r")

# Creates list based on f1 and f2
devices = host.readlines()
commands = cli.readlines()

for device in devices:
    device = device.rstrip()
    print ("host: ", device, "\n")
    for command in commands:
        command = command.rstrip()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read()
        print(" cli: \n", command,"\n")
        print(output)
        #data =[]
        #data.append(output)
        ssh.close()
host.close()
cli.close()
