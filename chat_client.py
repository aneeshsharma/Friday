import socket
from socket_connection import *

ip = input('IP: ')
port = int(input('Port: '))

sock = Socket()

sock.connect(ip, port)

while True:
	data = input('Msg: ')
	try:
		sock.send(data)
	except:
		print('Disconnected')
		break
	try:
		recv = sock.recv()
	except:
		print('Disconnected')
		break
	print('Rec:', recv)

sock.close()
