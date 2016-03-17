#! /usr/bin/python

import os
import subprocess

def getmac():
	try:
		mac = open('/sys/class/net/wlan0/address').readline()
	except:
		mac = "00:00:00:00:00:00"
	return mac[0:17]

def getip():
	a=os.popen('ifconfig wlan0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
	ip=a.read()[:-1]
	return ip

def getdiskusage():
        a=subprocess.check_output('df -m ~',shell=True)
        free=a.split()[-3]
        return free


def getram():
        a=subprocess.check_output('free -m',shell=True)
        free=a.split('\n')[1].split()[3]
        return free

def getwifistrength():
	try:
		a = open('/proc/net/wireless').read()
		link=a.split('\n')[2].split()[2][:-1]
	except:
		link='0'
	return str(int(int(link)*1.42857))

def Collect():
	a = getmac()
	b = getip()
	c = getdiskusage()
	d = getram()
	e = getwifistrength()
	return (a+' '+b+' '+c+' '+d+' '+e)
