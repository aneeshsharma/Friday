from SocketInterface import receive_pack, send_pack, Socket


def default_handler(sock, addr):
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


def socket_server(name, handler=default_handler):

    sock = Socket()

    port = sock.bind_port(7200, 8000)

    print(name, ': Listening to ', port)

    sock.listen_loop(5, handler)
