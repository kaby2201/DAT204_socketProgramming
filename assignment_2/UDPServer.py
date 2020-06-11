from socket import *


def main():
    SERVER_PORT = 1200

    # AF_INET is for IPv4 and SOCK_DGRAM is for UDP
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    serverSocket.bind(('', SERVER_PORT))
    print("The server is ready to receive")
    while True:
        message, client_address = serverSocket.recvfrom(2048)
        modified_message = message.decode().upper()
        serverSocket.sendto(modified_message.encode(), client_address)


if __name__ == '__main__':
    main()