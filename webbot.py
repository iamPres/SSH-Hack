import paramiko, os, socket, sys, random
count=0
sig="#"
for i in range(100000):
    count += 1
    print sig*count
    if count <= 10:
        os.system("python /users/prestonwillis/documents/python/sshhack_child.py &")
    elif count > 10:
        break;
print "[*] LOADING: Please wait"
