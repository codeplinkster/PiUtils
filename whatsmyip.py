#!/usr/bin/python3

from urllib.request import urlopen
import json
import socket

from tkinter import *

rootWindow = Tk()
rootWindow.title('My IP Addresses')

localIP = Label(rootWindow, font = ('fixed', 30),)
localIP.grid(sticky = N, row = 2, column = 1, padx = 5, pady = (30,30))
publicIP = Label(rootWindow, font = ('fixed', 30),)
publicIP.grid(sticky = N, row = 3, column = 1, padx = 5, pady = (30,30))
hostName = Label(rootWindow, font = ('fixed', 30),)
hostName.grid(sticky = N, row = 1, column = 1, padx = 5, pady = (30,30))

#read the public side ip address by using httpbin.org json return ip
ip = urlopen('http://httpbin.org/ip').read()
ip = ip.decode('utf-8')
ip = json.loads(ip)
testIP = "8.8.8.8"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((testIP, 0))
ipaddr = s.getsockname()[0]
host = socket.gethostname()
localIP.config(text="local ip:"+str(ipaddr))
publicIP.config(text=ip['origin'])
hostName.config(text=host)

rootWindow.mainloop()