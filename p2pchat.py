import socket
import thread

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def server():
	ss = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = 1337                # Reserve a port for your service.
	ss.bind((host, port))        # Bind to the port

	ss.listen(5)                 # Now wait for client connection.
	while True:
		c, addr = ss.accept()     # Establish connection with client.
		print bcolors.OKGREEN + ss.recv(1024) + bcolors.ENDC
		c.close()
		c, addr = ss.accept()
		print ss.recv(1024)
		c.close()

thread.start_new_thread( server )

sc = socket.socket()         # Create a socket object
username = "Taylor"
sc.connect((host, port))

while True:
	instr = raw_input( username  + "-> ")
	if(len(instr) > 1024)
		print "Max length is 1024 chars"
	else
		
sc.close                     # Close the socket when done
