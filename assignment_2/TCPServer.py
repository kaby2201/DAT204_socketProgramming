from socket import *


def main():
    # Create a TCP socket, AF_INET = IPv4 and SOCK_STREAM = TCP
    server_socket = socket(AF_INET, SOCK_STREAM)

    # Associate the server port with this socket
    SERVER_PORT = 12000
    server_socket.bind(('', SERVER_PORT))

    # Maximum number of queued connections
    server_socket.listen(1)
    print("The server is ready to receive")
    while True:
        # After invoking accept(), the server will creates a new socket
        connectionSocket, addr = server_socket.accept()
        sentence = connectionSocket.recv(1024).decode()

        print(f'Message from: {addr[0]}:{addr[1]}')
        print(f'Message: {sentence}')

        capitalizedSentence = sentence.upper()
        # After send back the next in capitalized
        connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()


if __name__ == '__main__':
    main()
