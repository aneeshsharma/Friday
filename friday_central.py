import socket_server
import socket_connection
import threading
import eliza

def eliza_bot(sock, addr):
    bot = eliza.eliza()
    print('Eliza : Connection Received -', sock.getpeername())
    data = b''
    while data != b'exit':
        try:
            data = socket_connection.receive_pack(sock)
            if data == b'exit':
                print('Eliza : Exit -', sock.getpeername())
                break
        except:
            print('Eliza : Disconnected -', sock.getpeername())
            break
        print('Eliza : Data Received: ', data)
        reply = bot.respond(str(data)).encode('utf-8')
        socket_connection.send_pack(sock, reply)
    sock.close()

command_server = threading.Thread(target=socket_server.socket_server, args=(eliza_bot,))

command_server.start()