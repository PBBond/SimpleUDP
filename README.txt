Server: server_simple_udp.py
Launch server from command line by specifiying the python script name and a port number as an argument.

Example command line:

server_simple_udp.py 556027

Once the server is running proceed to running the client script


Client: client_simple_udp.py
Send a file or piece of text to server and calculate the round trip time.
Client takes 3 arguments:
	1. The host IP
	2. Port
	3. File name or text

Example commande line:

client_simple_udp.py localhost 56027 File1.txt

or

client_simple_udp.py localhost 56027 "Sample text to send to server"



This can also be done in PyCharm by going to:
Run -> Edit Configurations -> Parameters

and listing the parameters in the input line. For server input one parameter which becomes the port number
for example 56027. For the client enter three parameters of host IP, port, filename or text. For example
localhost 56027 File1.txt

Launch the server script first, then run the client script afterwards.
