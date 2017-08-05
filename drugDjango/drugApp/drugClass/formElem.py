# -*- coding: utf-8 -*-
from drugApp.drugClass.searchElem import *
def  formElm():
	elemList=[]
	e0=searchElem("url", "eg:http://mp.weixin.qq.com/s/FFj-7dvWPJsUPojktW-qjQ")
	e1=searchElem("dictionlist", "eg:  1-27")
	e2=searchElem("removeDict", "eg:  0  、")
	e3=searchElem("tag", "eg:   section")
	e4=searchElem("drugInterLabel", "eg:  ,")
	e5=searchElem("drugByNameLabelList", "eg: （ ( ) ")
	elemList=[e0,e1,e2,e3,e4,e5]
	# searchList = ["url", "dictionlist", "removeDict", "tag", "drugInterLabel","drugByNameLabelList"]
	# showList=["eg:http://mp.weixin.qq.com/s/FFj-7dvWPJsUPojktW-qjQ","eg:  1-27","eg:  0  、","eg:   section","eg: （ ( ) "]

	return elemList