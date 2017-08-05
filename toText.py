from extractData import *

class  downTxtDrug(object):
	"""docstring for  downTxtDrug"""
	def __init__(self, dictDrug):
		super( downTxtDrug, self).__init__()
		self.dictDrug = dictDrug

	def  readTxt(filepath):
	file_object = open(filepath)
	try:
		all_the_text = file_object.read( )
	finally:
		file_object.close( )
	if  all_the_text:
		#print all_the_text
		
		return all_the_text
	else:
		return False


	def  writeTxt(filepath,drugDict):
		text=trasToText(nMatrix)
		f = open(filepath, 'a')
		f.write(text)
		f.close()
		
			

url="http://mp.weixin.qq.com/s/FFj-7dvWPJsUPojktW-qjQ"
sp=spider(url)
html=sp.getData()

dictionlist=[ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']

tag="section"
exdata=extractDrugs(html, tag, dictionlist)
drugDict=exdata.getDrug()
print drugDict
