# -*- coding: utf-8 -*-
import urllib,sys
def  proDL(data):
	datalist=data.split("-")
	
	dictionlist=[]
	for i in range(int(datalist[1])+1):
		if  i<  int(datalist[0]):
			continue
		dictionlist.append(str(i))
		
	return dictionlist

def  proRMBreak(data):
	datalist=data.split(" ")
	datalist=data.split(" ")
	return datalist

def toUrlCode(data):
	rdata=urllib.quote(data)
	return rdata
	#urllib.quote(s.decode(sys.stdin.encoding).encode('gbk'))
	#rdata=urllib.quote(data.decode(sys.stdin.encoding).encode('utf8'))
	
	
# a=[2]
# b=[1]
# c=a+b
# print c
# data="西妥昔单抗"
# drugname=toUrlCode(data)
# print drugname
# datalist=proDL(data)
# print datalist
# def  proTG(data):
# 	pass

# def  proDI(data):
# 	pass

# def  proDBN(data):

# 	pass

