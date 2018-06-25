import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com',80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0')
data=mysock.recv()
print (data)
mysock.close()        