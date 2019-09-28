from socket import *
import ssl
serverName = 'localhost'
serverPort = 8443
clientSocket = socket(AF_INET, SOCK_STREAM)
context = ssl.create_default_context(cafile="example.crt", capath=".")
sslSocket = context.wrap_socket(clientSocket, server_hostname=serverName)
sslSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
sslSocket.send(sentence.encode())
modifiedSentence = sslSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
sslSocket.close()
