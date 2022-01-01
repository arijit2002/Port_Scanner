import pyfiglet
import sys
import socket
from datetime import datetime

name = pyfiglet.figlet_format("JUST  SCAN  IT")
print(name)

ip_addr=input("Enter the IP address name: ")

# Defining a target
'''
if len(ip_addr) == 2:
	# translate hostname to IPv4
	target = socket.gethostbyname(ip_addr)

else:
	print("Invalid ammount of Argument")
'''
start_port=int(input("Enter starting port: "))
end_port=int(input("Enter ending port: "))

# Add Banner
print("-" * 50)
print("Scanning Target: " + ip_addr)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
	for port in range(start_port,end_port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		
		# returns an error indicator
		result = s.connect_ex((ip_addr,port))
		if result ==0:
			print("Port {} is open".format(port))
		else:
                        print("Port {} is closed or filtered".format(port))
		s.close()
		
except KeyboardInterrupt:
		print("\n Exitting Program !!!!")
		sys.exit()
except socket.gaierror:
		print("\n Hostname Could Not Be Resolved !!!!")
		sys.exit()
except socket.error:
		print("\ Server not responding !!!!")
		sys.exit()
