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
    wgs84_position = [47.22274, 8.81642]
    verbose = True


    def __init__(self, deviceId, hostName, sharedKey):
        self.deviceId = deviceId
        self.connectionString = self.connectionStringTemplate.format(hostName, deviceId, sharedKey)

    def hubConnect(self):
        self.iotHubClient = IoTHubClient(self.connectionString, self.protocol)
        self.iotHubClient.set_message_callback(self.hubMsgCallBack, None)

    def hubMsgCallBack(self, message, context):
        #get message as object
        buffer =  message.get_bytearray()
        size = len(buffer)
        strMessage =  buffer[:size].decode('utf-8')
        objMessage = json.loads(strMessage)

        parameter = objMessage["Parameters"]["arg0"]
        name = objMessage["Name"]

        funCallBack = self.callBacks[name]
        funCallBack(parameter)

        return IoTHubMessageDispositionResult.ACCEPTED

    def hubMsgConfirmCallBack(self, message, result, context):
        if self.verbose:
            print "ConfirmCallback:" + str(result)

    def buildDeviceInfoMessage(self):
        #Build object hierarchiy and convert to json
        msg_device_properties = {"DeviceID": self.deviceId, \
                      "HubEnabledState": True, \
                      "Latitude":  self.wgs84_position[0],\
                      "Longitude":  self.wgs84_position[1]\
                    }

        #build list with callbacks
        msg_commands = []
        for key in self.callBacks:
            msg_command_param = [{"Name": "arg0", \
                         "Type": "double"\
                        }]

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
        if self.verbose:
            print("Device state update")

        self.buildDeviceInfoMessage()


    def sendJSONMessage(self, data):
        if self.verbose:
            print("---- START MESSAGE -------")
            print json.dumps(data)
            print("----  END MESSAGE  -------")

        #send message using iothub
        hubMessage = IoTHubMessage(json.dumps(data))
        self.iotHubClient.send_event_async(hubMessage, self.hubMsgConfirmCallBack, None)

    def sendSensorData(self, name, value):
        msg = {"deviceId" : self.deviceId, \
            name : value}
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




