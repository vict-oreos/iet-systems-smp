import socket
HOST="127.0.0.1"
PORT=80
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST,PORT))
server.listen(5)
print("Server is waiting to accept a connection on "+HOST+":"+str(PORT))
connection, address = server.accept() 
print("Acepted connection from: " + str(address))
data = connection.recv(1024)
if data:
    print("Data received from client: "+data)
    connection.sendall(data)
    print("Data sent back to client: "+data)
else:
    print("Error: No data has been received as connection may be closed.")
connection.close()
server.close()
