import socket
import sys
import thread

def serveclient(c):
	global v,nclnt,vlock,nclntlock
	while 1:
		k = c.recv(1)
		if k == '':	
			break
		vlock.acquire()
		v+=k
		vlock.release()
		c.send(v)
	c.close()
	nclntlock.acquire()
	nclnt -=1
	nclntlock.release()
lstn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(sys.argv[1])
lstn.bind('', port)
lstn.listen(5)
v = ''
vlock = thread.allocate_lock()
nclnt = 2
nclntlock = thread.allocate_lock()
for i in range(nclnt):
	(clnt,ap) = lstn.accept()
	thread.start_new_thread(serverclient,(clnt,))
lstn.close()
while nclnt > 0:
	pass
print 'the final value of  v is',v


