import socket
import threading

def blank_handler(sock, addr):
	# Sample handler
	sock.send(b'Thank you for connecting')
	sock.close()


# Class to define socket connections
class Socket:
	def __init__(self):
		self.sock = socket.socket()
	
	def bind_port(self, port, max_port):
		while port <= max_port:
			try:
				self.sock.bind(('', port))
				break
			except socket.error:
				port += 1
		else:
			return -1
		return port
	
	def connect(self, ip, port):
		self.sock.connect((ip, port))

	def send(self, data, header=32):
		if type(data) != type(b''):
			data = data.encode('utf-8')
		return send_pack(self.sock, data, header)
	
	def recv(self, header=32):
		return receive_pack(self.sock, header)

	def listen_loop(self, num, handle_client=blank_handler):
		self.sock.listen(num)
		clients = []
		while True:
			client, addr = self.sock.accept()
			thread = threading.Thread(target=handle_client, args=(client, addr, ))
			thread.start()
			clients.append(thread)
	
	def close(self):
		del self

	def __del__(self):
		self.sock.close()

def send(sock, msg):
	total = 0
	MSGLEN = len(msg)
	while total < MSGLEN:
		sent = sock.send(msg[total:])
		if sent == 0:
			raise RuntimeError("Connection broken")
		total = total + sent
	return total

def receive(sock, MSGLEN):
	chunks = []
	received = 0
	MSGLEN = int(MSGLEN)
	while received < MSGLEN:
		chunk = sock.recv(min(MSGLEN - received, 1024))
		if chunk == b'':
			raise RuntimeError("Connection broken")
		chunks.append(chunk)
		received += len(chunk)
	return b''.join(chunks)

def receive_pack(sock, header=32):
	header = receive(sock, header)
	l = int(header[3:11].strip())
	data = receive(sock, l)
	return data

def send_pack(sock, data,  header=32):
	l = len(data)
	head = "MSG"+str(l)+" "*header
	head = head[0:header]
	head = head.encode('utf-8')
	if send(sock, head) == header:
		return send(sock, data)
	else:
		return -1
