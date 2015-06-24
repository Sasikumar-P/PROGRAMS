
# simple illustration of thread module

#two clients connect to server; each client repeatedly sends a letter,

#stored in the variable k, which the server appends to a global string
#v, and reports v to the client; k = ’’ means the client is dropping
#out; when all clients are gone, server prints the final string v
import sys
import sockect
s=socket.sockect(socket.AF_INET, socket.SOCK_STREAM)
host =sys.argv[1] #server addresss

port = int(sys.argv[2])# server port
s.connect(host, port)
while(1):
	k = raw_input("enter a letter")
	s.send(k)
	if k == '':
		break
	v=s.recv(1024)
	print v
s.close()


