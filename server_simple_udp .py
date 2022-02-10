#Name: Pavel Bondarenko
#StarID: bv2737dg
#Date: 2/8/2022
#Simple UDP client to handle receiving data and comparing the checksum
#to make sure data was properly received

import hashlib
from datetime import datetime
import socket
import json
import sys

#check for correct number of args
if (len(sys.argv) != 2):
    print("Incorrect number of arguments")
    print("Use: server_simple_udp.py <Port>")
    sys.exit()

#create socket and catch any errors
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    PORT = int(sys.argv[1])  # port is an argument
    IP = '127.0.0.1'  # localhost
    s.bind((IP, PORT))
except socket.error:
    print("Error creating socket")
    sys.exit(1)

print("Server is ready to receive on port ", PORT)
while True:
    print("Waiting...")
    msg, clientAddress = s.recvfrom(4096)
    timeReceived = datetime.now() # time that the message is received
    print("Received time: ", timeReceived)

    j = json.loads(msg.decode()) # decode the dictionary and turn it into json file
    data = j['data'] # get the message
    clientChecksum = j['checksum'] # get the checksum
    print("Message: ", data)
    print("Received checksum: ", clientChecksum)

    # create checksum of data received
    serverChecksum = hashlib.md5(data.encode()).hexdigest()
    print("Calculated checksum: ", serverChecksum)

    #if checksums match send the date back, otherwise send 0
    if clientChecksum == serverChecksum:
        s.sendto(str(timeReceived).encode(), clientAddress)
    else:
        s.sendto(str(0).encode(), clientAddress)




