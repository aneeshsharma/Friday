from socket_connection import *

def handle2(sock, addr):
	print('Connection Received -', sock.getpeername())
	data = b''
	while data != b'exit':
		try:
			data = receive_pack(sock)
			if data == b'exit':
				print('Disconnected -', sock.getpeername())
				break
		except:
			print('Disconnected -', sock.getpeername())
			break
		print('Data Received: ', data)
		send_pack(sock, data)
	sock.close()

sock = Socket()

port = sock.bind_port(7200, 8000)

print('Listening to ', port)

sock.listen_loop(5, handle2)

