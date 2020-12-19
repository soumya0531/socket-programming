import sys
import socket
import select
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',8000))
sys.stdout.write("Enter text: ")
sys.stdout.flush()
while True:
    listed=[sys.stdin,client]
    read,write,error=select.select(listed,[],[])
    for i in read:
        if i==client:
            message=i.recv(2048)
            message=str(message)[1:][1:-1]
            sys.stdout.flush()
            sys.stdout.write("Response from server: ")
            sys.stdout.write(message+"\n")
            sys.stdout.write("Enter text: ")
            sys.stdout.flush()
        else:
            message=sys.stdin.readline()
            res=message.encode('utf-8')
            sys.stdout.flush()
            client.send(res)
client.close()

