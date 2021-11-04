from socket import*

serverPort = 12000          # server port number
serverSocket = socket(AF_INET, SOCK_DGRAM)      # server socker AF_INET for IPv4, _DGRAM for UDP
serverSocket.bind(('localhost', serverPort))    # bind the host and port
print("This server is ready to receive\n")      # ready to receive
while True:                                     # infinite loop to receive and send
    message, clientAddress = serverSocket.recvfrom(2048)        # receive from client messege, and IP address, msg length 2048
    modifiedMessage = message.decode().upper()                  # decode received msg, and change to upper case letters
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)    # resend the information to client


# Code Used from PowerPoint Provided by Professor