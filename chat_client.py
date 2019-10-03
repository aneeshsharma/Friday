import socket
from socket_connection import *

ip = input('IP: ')
port = int(input('Port: '))

sock = Socket()

sock.connect(ip, port)

while True:
	data = input('You:\t')
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
	print('\033[1;34mFriday:\t', recv.decode('utf-8') + '\033[0;37m')

sock.close()
