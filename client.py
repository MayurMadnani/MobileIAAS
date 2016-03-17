#! /usr/bin/python

HOST = "192.168.43.236"
PORT = 12345

from clientdata import Collect
import socket

host = HOST
port = PORT
s = socket.socket()
s.connect((host, port))
data = Collect()
s.send(data)
s.close()
