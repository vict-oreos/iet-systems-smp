import socket
HOST="127.0.0.1"
PORT=80
MESSAGE="Message to be sent to and received from server."
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
print("Client is connected to server at "+HOST+" "+str(PORT))
message=MESSAGE.encode()
client.sendall(message)
print("Client has sent data to server")
rec_in_bytes=client.recv(1024)
received=rec_in_bytes.decode()
print("Echo received from server: "+received)
client.close()