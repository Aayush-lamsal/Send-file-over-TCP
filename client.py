import socket 
# Creating Client Socket 
if __name__ == '__main__': 
	host = '127.0.0.1'
	port = 8880

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Connecting with Server 
	sock.connect((host, port)) 

	while True: 

		filename = input('Input filename you wanna  to send: ') 
		try: 
		# Reading file and sending data to server 
			fi = open(filename, "r")
			print(filename) 
			data = fi.read() 
			if not data: 
				break
			while data: 
				sock.send(str(data).encode()) 
				data = fi.read() 
			# File is closed after data is sent 
			fi.close() 

		except Exception as e:
			print(e)
