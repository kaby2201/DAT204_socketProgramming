from socket import *


def main():
    # AF_INET is IPv4 and Socket_stream  is TCP
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Before sending data we must establish a TCP connection
    SERVER_NAME = 'localhost'
    SERVER_PORT = 12000

    try:
        clientSocket.connect((SERVER_NAME, SERVER_PORT))

        # Get user input
        sentence = input('Input lowercase sentence: ')

        # Send sentence through the client's socket into the TCP connection
        clientSocket.send(sentence.encode())

        # recvfrom takes buffer size
        modifiedSentence = clientSocket.recv(1024)

        # Print out the modified sentence
        print(modifiedSentence.decode())

        # close the socket connection
        clientSocket.close()
    except:
        print('Make sure the server is open at the specified port number')


if __name__ == '__main__':
    main()
