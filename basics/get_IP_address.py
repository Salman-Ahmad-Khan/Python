import socket
hostname=socket.gethostname()
IP_address=socket.gethostbyname(hostname)
print("IP address is: ",IP_address)