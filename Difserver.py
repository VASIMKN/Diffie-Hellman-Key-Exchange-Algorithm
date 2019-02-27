import socket
import random
import math
import primroots

#server = A

server = socket.socket()
server.bind(('localhost',5050))
server.listen(10)
conn, address = server.accept()



q,alpha=primroots.primeRoot()

conn.send(str(q).encode())
conn.send(str(alpha).encode())

print("q :",q)
print("alpha :",alpha)

xa,ya=primroots.Xab(q,alpha)
print("Xa :",xa)
print("Ya :",ya)

conn.send(str(ya).encode())

yb = int((conn.recv(1024)).decode())
print("Yb :",yb)

ka=primroots.key(yb,xa,q)
print("Ka :",ka)
