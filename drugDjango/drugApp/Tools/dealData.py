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
	
# data="1-27"
# datalist=proDL(data)
# print datalist
# def  proTG(data):
# 	pass

# def  proDI(data):
# 	pass

# def  proDBN(data):

# 	pass

