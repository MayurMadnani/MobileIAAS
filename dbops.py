#! /usr/bin/python

import sqlite3
import os
from tabulate import tabulate

def createTable():
	conn = sqlite3.connect('db')
	conn.execute('''CREATE TABLE clientdata
	       (mac varchar PRIMARY KEY NOT NULL,
		ip varchar NOT NULL,
	       disk int NOT NULL,
	       ram int NOT NULL,
		wifi int NOT NULL,
		alive char NOT NULL);''' )
	conn.close()

def select():
	conn = sqlite3.connect('db')
	cursor = conn.execute("SELECT mac,ip,disk,ram,wifi,alive from clientdata")
	table=[]
	print ""
	for row in cursor:
  		table.append([str(i) for i in row])
	print tabulate(table,headers=["MAC","IP","Disk","RAM","WiFi","Alive"],tablefmt="grid")
	conn.close()


def pingips():
	conn = sqlite3.connect('db')
	cursor = conn.execute("SELECT ip  from clientdata")
	a=[str(r[0]) for r in cursor.fetchall()]
	return a

def topk(k):
	conn = sqlite3.connect('db')
	cursor = conn.execute("SELECT ip from clientdata where alive='Y' and wifi>40 order by disk desc limit(?)",(str(k)))
	ips=[]
	for row in cursor:
       		ips.append(row[0])
	return ips
	conn.close()

def insert(mac,ip,disk,ram,wifi):
	conn = sqlite3.connect('db')
	try:
		conn.execute("INSERT INTO clientdata (mac,ip,disk,ram,wifi,alive) VALUES (?,?,?,?,?,'Y')",(mac,ip,disk,ram,wifi));
	except:
		conn.close()
		update(mac,ip,disk,ram,wifi,'Y')
		return
	conn.commit()
	conn.close()

def update(mac,ip,disk,ram,wifi,alive):
	conn = sqlite3.connect('db')
	conn.execute("UPDATE clientdata set ip=?,disk=?,ram=?,wifi=?,alive=? where mac=?",(ip,disk,ram,wifi,alive, mac))
	conn.commit()
	conn.close()

def updatedead(ip):
	conn = sqlite3.connect('db')
	conn.execute("UPDATE clientdata set alive='N' where ip=?",(ip,))
	conn.commit()
	conn.close()
