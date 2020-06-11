from socket import *


def main():
    # AF_INET indicates the that we are using IPv4
    # SOCK_DGRAM means it is a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Get user input
    message = input('Input lowercase sentence: ')

    SERVER_NAME = 'localhost'
    SERVER_PORT = 1200
    # Convert the message from string type to byte type
    # function clientSocket(messenge in byte, (servername, portnamuber)
    clientSocket.sendto(message.encode(), (SERVER_NAME, SERVER_PORT))

    # After sending packet above, the the packet data, will med put in modifiendMessage,
    # the variable serverAddress contains both server IP and port number
    # recvfrom takes buffer size
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    # read the converting the modifiedMessage and print it out
    print(modifiedMessage.decode())

    # closes the socket
    clientSocket.close()


if __name__ == '__main__':
    main()
