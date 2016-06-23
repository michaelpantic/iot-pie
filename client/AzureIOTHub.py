class AzureIOTHub:
	deviceId = ""
	hostname = ""

	callBacks = {}

	def __init__(self, deviceId, hostname):
		self.deviceId = deviceId
		self.hostname = hostname

	def updateDeviceState(self):
		print("Device state update")

	def sendJSONMessage(self, data):
		print("JSON")

	def sendSensorData(self, dictionary):
		for key in dictionary:
			print key,"=",dictionary[key]

		print self.deviceId


	def registerCallBack(self, function, command):
		self.callBacks[command] = function
	
		
	def simulateCallBack(self, command, argument):
		function = self.callBacks[command]
		function(argument)
		




