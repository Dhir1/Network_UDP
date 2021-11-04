# Include socket and date libraries
from socket import *

'''-------------------------------Open BMP file from certain path-----------------
    You can specify anyfile path, any filename, must be .bmp format
'''
filePath = "./"
fileName = "receivedSample_BMP.bmp"
file = open(filePath + fileName, 'ab')


'''------------------------Function to extract the packets, and append data---------'''
def extract(packet, data):
    data.extend(packet)        

'''-----------------------Receive the data, write to file---------------------'''
def receive_data(data):
    bytes_data = bytes(data)    
    file.write(bytes_data)        

'''---------------------Start Server Function--------------------'''
def START_SERVER():
    receivedData = []
    terminate_msg = "end_of_packet"
    packetCounts = 0

    '''
        Socket Details
    '''
    serverPort = 12000
    serverHost = 'localhost'
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind((serverHost, serverPort))
    print("SERVER STATUS: READY")

    while True:                                                 # infinte loop to start receving data
        message, clientAddress = serverSocket.recvfrom(2048)    # receive from client

        print(f"Packet Number: {packetCounts}")                 # packet number from client

        receiveStatus = "SUCCESSFULLY RECEIVED"                 # reply the status
        print(f"STATUS: {receiveStatus}")
        serverSocket.sendto(receiveStatus.encode(), clientAddress)  # send to clietn
        # packetCounts += 1
        extract(message, receivedData)                          # extract and append data

        if message == terminate_msg.encode():                          # if terminating code is received, break the loop
            break
        packetCounts += 1

    receive_data(receivedData)                                  # write data
    file.close()                                                # close file
    print("CONNECTION CLOSED")                                  # clode connection

if __name__ == '__main__':
    START_SERVER()