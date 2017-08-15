# Simple_scanner.py

This script is just a PoC to use python socket module and of course use any other decent port scanner rather than this one, like for example nmap.

### Usage

The simple_scanner.py accepts 3 arguments:

* -t is for the target host that can be a list of IP or FQDN, separated by BLANK spaces.
* -p is for the ports, you can add as much of them as you like, separated by BLANK spaces.
* -s is OPTIONAL to specify the timeout for the socket, by default is 5 seconds.

First grant execution permissions

```
chmod +x simple_scanner.py
```

You can always run the help

```
./simple_scanner.py -h
```

#### Examples

```
$ ./simple_scanner.py -t google.com nasa.org -p 80 443 8080 -s 15
[+] INFO: Scanning host google.com
        [+] INFO: Port 443 is open
        [+] INFO: Port 80 is open
        [!] WARNING: timed out Can not connect to port 8080
[+] INFO: Scanning host nasa.org
        [+] INFO: Port 443 is open
        [+] INFO: Port 80 is open
        [!] WARNING: timed out Can not connect to port 8080
``` 

