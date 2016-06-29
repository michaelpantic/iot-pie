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
        msg_device_properties = {"DeviceID": deviceID \
                                 "HubEnabledState": true \
                                }

        #build list with callbacks
        msg_commands = []
        for key in callBacks:
            msg_command_param = {"Name": "arg0" \
                                 "Type": "double"\
                                }

            msg_commands.append({"Name": key \
                                 "Parameters" : msg_command_param \
                                }

        msg_header_obj = {"ObjectType": "DeviceInfo", \
                          "Version": "1.0", \
                          "IsSimulatedDevice" : False \
                          "DeviceProperties" : msg_device_properties \
                          "Commands" : msg_commands \
                         }
        print json.dumps(msg_header_obj)


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





