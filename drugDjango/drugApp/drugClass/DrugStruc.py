class  drug(object):
	"""docstring for  drug"""
	def __init__(self, drugname,drugByname,drugClass):
		
		self.drugname = drugname
		self.drugByname = drugByname
		self.drugClass = drugClass
	
class  drugSearch(object):
	"""docstring for  drug"""
	def __init__(self, newdrugname,alreadydrugname,cantdrugname):
		
		self.newdrugname = newdrugname
		self.alreadydrugname = alreadydrugname
		self.cantdrugname = cantdrugname

class  dFeature(object):
	"""docstring for  drug"""
	def __init__(self, feature,featureNum,drugs,subfeatures):
		
		#self.drugname = drugname
		self.feature = feature
		self.featureNum = featureNum 
		self.drugs=drugs #[ ]
		self.subfeatures=subfeatures #[ ]
 