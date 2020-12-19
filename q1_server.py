import socket
from _thread import *
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('localhost',8000))
server.listen(1)
print("Server is listening at : localhost:8000")
list_clients=[]
def clientthread(con,adr):
    while True:
        try:
            message=con.recv(2048)
            if message:
                message = str(message)
                message = message[1:][1:-3]
                print('[client]:' + message)
                message = message[::-1]
                response = ''
                for ch in message:
                    if(ord(ch) >= 97 and ord(ch) <= 97+25):
                        response += chr(ord(ch) - 32)
                    elif(ord(ch) >= 64 and ord(ch) <= 64+25) :
                        response += chr(ord(ch) + 32)
                    else:
                        response += ch
                res = response.encode('utf-8')
                con.send(res)
            else:
                remove(con)
        except:
            continue
def remove(connection):
    if connection in list_clients:
        list_clients.remove(connection)
while True:
    conn,adrr=server.accept()
    list_clients.append(conn)
    print("connected : "+adrr[0])
    start_new_thread(clientthread,(conn,adrr))
conn.close()
server.close()