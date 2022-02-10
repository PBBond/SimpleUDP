#Name: Pavel Bondarenko
#StarID: bv2737dg
#Date: 2/8/2022
#Simple UDP client script to send a file or text to a server and calculate RTT

import sys
import socket
from datetime import datetime
import hashlib
import json

#check for correct number of args
if (len(sys.argv) != 4):
    print("Incorrect number of arguments")
    print("Use: client_simple_udp.py <Server Host> <Port> <File or message>")
    sys.exit()

IP = sys.argv[1]
PORT = int(sys.argv[2])
filename = sys.argv[3]
#create socket and catch errors
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print("Error creating socket")
    sys.exit(1)
#function to check for file or string argument
def getMessage(argument):
    if argument[-4:] == '.txt':
        f = open(filename, 'r').read()
        return f
    else:
        return argument

#get the file contents or the string from argument
msg = getMessage(filename)
#create checksum of data to send
checksum = hashlib.md5(msg.encode()).hexdigest()
print("Checksum sent: ", checksum)
#turn the message and checksum into a dictionary (object)
msgChecksum = {
    "data": msg,
    "checksum": checksum
}
#turn object into string and encode
encodedMsg = json.dumps(msgChecksum).encode()

#check for file length
if len(encodedMsg) <= 4096:
    t1 = datetime.now()
    print("Time message was sent: ", t1)
    s.sendto(encodedMsg, (IP, PORT)) #send the object to server

    try:
        received, addr = s.recvfrom(4096)  # receive message back
        t2 = datetime.now()
        # if message is 0, message failed, otherwise it was successful
        if received.decode() == '0':
            print('Message failed!')
        else:
            print("Server has successfully received message at: ", received.decode())
            print("RTT: ", (t2 - t1).microseconds, " microseconds")
    except socket.timeout:
        print("Request timed out")
else:
    print("message length too big")


