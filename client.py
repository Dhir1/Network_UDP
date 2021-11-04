# Include socket and date libraries
from socket import *

'''DEFINED PACKET SIZE'''
PACKET_SIZE = 1500 #bytes

'''-------------------------------Open BMP file from certain path-----------------
    You can specify anyfile path, any filename, must be .bmp format
'''
filePath, fileName = "./", "sample_bmp.bmp"
file = open(filePath + fileName, 'rb')
fileData = file.read()
fileSize = len(fileData)



'''-------------------------------Socket Details----------------------------------'''
serverName, serverPort = 'localhost', 12000
serverInfo = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)  
print("CONNECTION STATUS: CONNECTED")

'''-------------------------------Make Packet Function----------------------------'''
def make_packet(data):
    dataOffset, packetNum = 0, 0
    while dataOffset < len(data):
        if dataOffset + PACKET_SIZE > len(data):
            packet = fileData[dataOffset:]
        else:
            packet = fileData[dataOffset:dataOffset + PACKET_SIZE]
        dataOffset += PACKET_SIZE
        send_data(packet, packetNum)
        packetNum += 1

'''-------------------------------Send Data-------------------------------
    sending the packet to server
'''
def send_data(packet, packetNum):
    clientSocket.sendto(packet, serverInfo)                                         # stat sending packet
    print(f"Sending Packet {packetNum}")       # printing info
    receiverMessage, recieverAddress = clientSocket.recvfrom(2048)                  # receive response from server
    print(f"Packet {packetNum},  {receiverMessage.decode()}")  # printout response
    

if __name__ == '__main__':
    print (f'Filename: {fileName}')                         # print out file name
    print (f'File Size: {fileData} bytes')                  # print out file size
    make_packet(fileData)                                   # make packets of sending image
    terminate_msg = "end_of_packet"                         # to denote that no more packeting is coming
    clientSocket.sendto(terminate_msg.encode(), serverInfo) # send to server
    # time.sleep(1)   
    clientSocket.close()
    file.close()
    print("CONNECTION CLOSED")
