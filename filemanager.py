#! /usr/bin/python

from fileops import FileManager

test=FileManager()
test.filepath="/home/mayur/mobileiaas/files/"
test.filename="demo.ogg"
test.backuppath="/home/mayur/mobileiaas/backup/"
test.k=2
test.n=3

test.init()
test.encode()
test.send()
wait=raw_input()
test.recv()
test.decode()
