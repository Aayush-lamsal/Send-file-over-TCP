import socket
import signal
import sys

# Function to handle signals and exit gracefully
def signal_handler(sig, frame):
    print(f"Received signal {sig}. Exiting gracefully.")
    # Closing all Connections
    for conn in connections:
        conn.close()
    sys.exit(0)

if __name__ == '__main__':
    # Register the signal handler for both SIGQUIT and SIGTERM
    signal.signal(signal.SIGTERM, signal_handler)
	
    # Here I have Defined Socket
    host = '127.0.0.1'
    port = 8880
    totalclient = int(input('Enter number of clients: '))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))

    sock.listen(totalclient)
    # socket connection for the limitation  to only 10 second
    sock.settimeout(10)  # Set a timeout of 10 seconds for the connection attempt

    # Creating Connection
    connections = []
    print('Initiating clients')
    for i in range(totalclient):
        try:
            #  while occuring connection error point 1
            conn, addr = sock.accept()
            connections.append(conn)
            print('Connected with client', i + 1)
        except socket.timeout:
            #point 1 to auto terminate the connection
            print(f'Timeout occurred while waiting for client {i + 1}')
            break

    fileno = 0
    idx = 0
    for conn in connections:
        # Receiving File Data
        idx += 1
        # data limitation has been limited to 1 mb ,,and it is ato terminated if this coindition appears to trye as per the module
        data = conn.recv(1024).decode()

        print(data)

        if not data:
        #  while occuring data transmission error point 5
         print("No data found")
        else:
        
            # Creating new file at the server and writing the data
            filename = 'output' + str(fileno) + '.txt'
            fileno = fileno + 1
            fo = open(filename, "w")
            while data:
                if not data:
                    break
                else:
                    fo.write(data)
                    data = conn.recv(1024).decode()
                   

            print('Receiving file from client', idx)
        # print()
            print('Received successfully! New filename is:', filename)
            #  after successfull terminate with code 0 point 3
            sys.exit(0)
            fo.close()

    # Exit gracefully when receiving signals
# signal.pause()
	