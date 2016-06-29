import json

class AzureIOTHub:
	deviceId = ""
	hostname = ""

	callBacks = {}

	def __init__(self, deviceId, hostname):
		self.deviceId = deviceId
		self.hostname = hostname

	def buildDeviceInfoMessage(self):
		#Build object hierarchiy and convert to json
		msg_device_properties = {"DeviceID": self.deviceId, \
				 	 "HubEnabledState": True \
					}

		#build list with callbacks
		msg_commands = []
		for key in self.callBacks:
			msg_command_param = {"Name": "arg0", \
	 				    "Type": "double"\
						}

		msg_commands.append({"Name": key, \
				     "Parameters" : msg_command_param \
				    })
		#assemble message
		msg_header_obj = {"ObjectType": "DeviceInfo", \
				"Version": "1.0", \
				"IsSimulatedDevice" : False, \
			 	"DeviceProperties" : msg_device_properties, \
				"Commands" : msg_commands \
				 }

		#send message
		self.sendJSONMessage(msg_header_obj)
		
	def updateDeviceState(self):
		print("Device state update")
		self.buildDeviceInfoMessage()


	def sendJSONMessage(self, data):
		print("---- START MESSAGE -------")
		print json.dumps(data)
		print("----  END MESSAGE  -------")

	def sendSensorData(self, name, value):
		msg = {"deviceId" : self.deviceId, \
			name : value,\
		      }
		self.sendJSONMessage(msg)

	def sendMultipleSensorData(self, dictionary):
		# reuse data dictionary as message
		dictionary["deviceId"] = self.deviceId
		self.sendJSONMessage(dictionary)


	def registerCallBack(self, function, command):
		self.callBacks[command] = function

	def simulateCallBack(self, command, argument):
		function = self.callBacks[command]
		function(argument)





