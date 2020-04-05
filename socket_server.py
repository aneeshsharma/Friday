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


def socket_server(name, handler=default_handler, port_start=7200, port_end=8000):

    sock = Socket()

    port = sock.bind_port(port_start, port_end)

    print(name, ': Listening to ', port)

    sock.listen_loop(5, handler)
