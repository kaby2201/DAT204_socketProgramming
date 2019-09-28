from socket import *
from ssl import create_default_context, Purpose

serverPort = 8443
context = create_default_context(Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='example.crt', keyfile='example.key')
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket .setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connSock, addr = serverSocket.accept()
    sslSocket = context.wrap_socket(connSock, server_side=True)
    sentence = sslSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    sslSocket.send(capitalizedSentence.encode())
    sslSocket.shutdown(SHUT_RDWR)
    sslSocket.close()
