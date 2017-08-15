#!/usr/bin/env python
#Script to just scan ports

import socket
import sys
import argparse

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
B = '\033[34m' # blue

#Argument parsing
help_message = ("USAGE:\n" +
                "The simple_scanner.py checks ports for TCP connections only\n" +
				"Example:\n" +
				"simple_scanner.py -t localhost google.fr -p 21 22 8200 -s 20") 
parser = argparse.ArgumentParser(usage=help_message, description='Scan TCP ports')
parser.add_argument('-t', help='FQDN or IP of the target host, separated by blank spaces', default=False, nargs='*')
parser.add_argument('-p', help='Blank space separated list of ports', default=False, nargs='*')
parser.add_argument('-s', help='Optional, seconds for timeout by default is 5', default=5)
args = parser.parse_args()


if __name__ == "__main__":

	hosts = set(args.t)
	ports = set(args.p)
	timeout = float(args.s)

	#Loop through the hosts
	for host in hosts:
		print G + '[+] INFO: Scanning host {}'.format(host) + W
		#Loop through the ports
		for port in ports:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			except socket.error as msg:
				print R + '[-] ERROR: Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1] + W
				sys.exit(69)

			s.settimeout(timeout)

			try:	
				s.connect((host,int(port)))
				print G + "\t[+] INFO: Port {} is open".format(port) + W

			except Exception as msg:
			#except socket.error, exc:
				print R + "\t[!] WARNING: {} Can not connect to port {}".format(msg, port) + W

			s.close()

