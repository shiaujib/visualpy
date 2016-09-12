#!/usr/bin/python 
# -*- coding: utf-8 -*-

from socket import *
import struct
SIZE=1000
sensor1=[]*SIZE
sensor2=[]*SIZE
sensor3=[]*SIZE
sensor4=[]*SIZE
sensor5=[]*SIZE
sensor6=[]*SIZE
sensor7=[]*SIZE
sensor8=[]*SIZE
sensor9=[]*SIZE
sensor10=[]*SIZE
def client():
    ADDR = ('192.168.211.131',8000)
    recvSock = socket(AF_INET,SOCK_STREAM)
    recvSock.connect(ADDR)
    index=0
    BUFSIZE=1024
    print "receiving file..."
    while 1:
        if index<300000:
            message=recvSock.recv(BUFSIZE)
            print ('%s' %message)
        else:
            break
        index=index+1

    print "Already received file，disconnecting..."
    recvSock.close()
    print "close connection..."

if __name__=="__main__":
    client()
