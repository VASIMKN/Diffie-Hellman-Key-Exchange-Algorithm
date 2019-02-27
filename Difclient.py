import socket
import primroots

#Client = B
client = socket.socket()
client.connect(('localhost',5050))


q = int((client.recv(1024)).decode())
alpha = int((client.recv(1024)).decode())
#print("q :",q)
#print("alpha :",alpha)


xb,yb=primroots.Xab(q,alpha)
print("Xb :",xb)
print("Yb :",yb)

ya=int((client.recv(1024)).decode())
print("Ya :",ya)

client.send(str(yb).encode())

kb=primroots.key(ya,xb,q)
print("Kb :",kb)


