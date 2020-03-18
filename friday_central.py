import socket_server
import SocketInterface
import threading
import eliza


def eliza_bot(sock, addr):
    bot = eliza.eliza()
    print('Eliza : Connection Received -', sock.getpeername())
    data = b''
    while data != b'exit':
        try:
            data = SocketInterface.receive_pack(sock)[0]
            if data == b'exit':
                print('Eliza : Exit -', sock.getpeername())
                break
        except:
            print('Eliza : Disconnected -', sock.getpeername())
            break
        print('Eliza : Data Received: ', data)
        reply = ('Eliza:' + bot.respond(data.decode('utf-8'))).encode('utf-8')
        SocketInterface.send_pack(sock, reply)
    sock.close()


def discord_bot(sock, addr):
    bot = eliza.eliza()
    print('Eliza : Connection Received -', sock.getpeername())
    data = b''
    while data != b'exit':
        try:
            data = SocketInterface.receive_pack(sock)[0]
            if data == b'exit':
                print('Eliza : Exit -', sock.getpeername())
                break
        except:
            print('Eliza : Disconnected -', sock.getpeername())
            break
        print('Eliza : Data Received: ', data)
        reply = (bot.respond(data.decode('utf-8'))).encode('utf-8')
        SocketInterface.send_pack(sock, reply)
    sock.close()


discord_bot_server = threading.Thread(
    target=socket_server.socket_server, args=('Friday Discord Server', discord_bot,))

command_server = threading.Thread(
    target=socket_server.socket_server, args=('Eliza', eliza_bot,))

command_server.start()
discord_bot_server.start()
