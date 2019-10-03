import socket_server
import threading

command_server = threading.Thread(target=socket_server.socket_server, args=())

command_server.start()