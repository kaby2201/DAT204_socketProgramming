from socket import *
# Listen port
serverPort = 12000

# Create a TCP socket, AF_INET = IPv4 and SOCK_STREAM = TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Associate the server port with this socket
serverSocket.bind(('', serverPort))

# Maximum number of queued connections
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    # After invoking accept(), the server creates a new socket
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    # After send back the next in capitalized
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()