from socket import*

serverName = "localhost"    # servername
serverPort = 12000          # serverport
clientSocket = socket(AF_INET, SOCK_DGRAM)  # create client socket
message = input('type something in samll letters\n')    # prompt user to input
clientSocket.sendto(message.encode(), (serverName, serverPort)) #send to server
modifiedMessage, serveAddress = clientSocket.recvfrom(2048)     #receive what server resend

print(modifiedMessage.decode())     # decode & print what server resend
clientSocket.close()                # close the client socket

# Code Used from PowerPoint Provided by Professor