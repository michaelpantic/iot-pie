import json
import random
import time
import sys
import iothub_client
from iothub_client import *

class AzureIOTHub:
	deviceId = ""
    connectionStringTemplate = "HostName={0};DeviceId={1};SharedAccessKey={2}"
	connectionString = ""
	protocol = IoTHubTransportProvider.AMQP
	iotHubClient = None
	callBacks = {}


	def __init__(self, deviceId, hostName, sharedKey):
		self.deviceId = deviceId
		self.connectionString = connectionStringTemplate.format(hostName, deviceId, sharedKey)

	def hubConnect(self):
		#(connectionString, protocol) = get_iothub_opt("?", connection_string, protocol)
		self.iotHubClient = IoTHubClient(self.connection_string, self.protocol)
		self.iotHubClient.set_message_callback(self.hubMsgCallBack)

	def hubMsgCallBack(self, message):
		msg_properties = message.properties
		msg_key_value = msg_properties.get_internals()
		print msg_key_value

		#todo add code to get messages for callback

		return IoTHubMessageDispositionResult.ACCEPTED

	def hubMsgConfirmCallBack(self, message, result):
		print "ConfirmCallback:" + str(result)

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

		#send message using iothub
		hubMessage = IoTHubMessage(json.dumps(data))
		self.iotHubClient.send_event_async(message, self.hubMsgConfirmCallBack)

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




