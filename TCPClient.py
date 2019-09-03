from socket import *
serverName = '88.90.135.90'
serverPort = 1200
# AF_INET = IPv4
# Socket_stream  = TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Before sending data we must establish a TCP connection
clientSocket.connect((serverName, serverPort))

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