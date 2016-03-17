#! /usr/bin/python

from pinger import Pinger
from dbops import pingips,updatedead,select

ping = Pinger()
ping.thread_count = 4
ping.hosts = pingips()
nodes=ping.start()
for ip in nodes['dead']:
	updatedead(ip)
select()
