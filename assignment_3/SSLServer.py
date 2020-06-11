from socket import *
from ssl import create_default_context, Purpose


def main():
    context = create_default_context(Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='example.crt', keyfile='example.key')
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # all interface at server_port
    SERVER_PORT = 8444
    server_socket.bind(('', SERVER_PORT))
    server_socket.listen(1)
    print(f'Server is now running at port {SERVER_PORT} and is ready to client receive message.')

    while True:
        connSock, addr = server_socket.accept()
        sslSocket = context.wrap_socket(connSock, server_side=True)
        sentence = sslSocket.recv(1024).decode()

        print(f'Message from: {addr[0]}:{addr[1]}')
        print(f'Message: {sentence}')

        capitalizedSentence = sentence.upper()
        sslSocket.send(capitalizedSentence.encode())
        sslSocket.shutdown(SHUT_RDWR)
        sslSocket.close()


if __name__ == '__main__':
    main()
