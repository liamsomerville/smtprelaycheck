#!/usr/bin/python
#Import our Modules
import socket
import smtplib
from smtplib import *

#Set our variabls
Target = raw_input("Enter Ip address you wish to check: ")
Port = "25"
EmailFrom = raw_input("From: ")
EmailTo = raw_input("TO: ")

# Build our Connector
s = socket.socket()
s.connect((Target,int(Port)))
socket.setdefaulttimeout(3)
answer = s.recv(1024)


if ("220" in answer):
    print "\n[+]Port" + " " + str(Port) + " " + "Looks like port", Port, "is open on ", Target, "\n"
    smtpserver = smtplib.SMTP(Target,int(Port))
    r = smtpserver.docmd("Mail From:",EmailFrom)
    a = str(r)
    if ("250" in a):
        r = smtpserver.docmd("RCPT TO:",EmailTo)
        a = str(r)
        if ("250" in a):
	# if code 250 print results
            print "[+] The target looks like it is vulenarble to an open relay attack"
	else:
            print "[-] The target doesn't look vulnerable to an open relay attack "
else: # If we dont get a code 220 
    print "[-] Looks like the port maybe closed/Filtered"
