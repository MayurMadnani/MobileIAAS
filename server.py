#! /usr/bin/python

from dbops import createTable,insert
import socket 
import os

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind(('', port))
s.listen(5)
createTable()
while True:
	c, addr = s.accept()
	data=c.recv(47)
	mac,ip,disk,ram,wifi=data.split()
	insert(mac,ip,disk,ram,wifi)
	c.close()
