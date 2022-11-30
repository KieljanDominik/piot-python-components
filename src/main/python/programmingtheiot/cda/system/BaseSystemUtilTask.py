#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import src.main.python.programmingtheiot.common.ConfigConst as ConfigConst

class BaseSystemUtilTask():
	"""
	Shell implementation representation of class for student implementation.
	
	"""
	
	def __init__(self, name = ConfigConst.NOT_SET, typeID = ConfigConst.DEFAULT_SENSOR_TYPE):
		self.ID = typeID
		self.name=name
	
	def getName(self) -> str:
		return self.name
		pass
	
	def getTypeID(self) -> int:
		return self.ID
		pass
	
	def getTelemetryValue(self) -> float:
		pass
	