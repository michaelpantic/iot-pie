#!/usr/bin/env python
from AzureIOTHub import AzureIOTHub
#from PWMServo import PWMServo
import sys
#import Adafruit_DHT
import time
import getopt

dhtType = 11
dhtPin = 17
deviceId = ""
hostName = ""
sharedKey = ""

def setServoCallBack(angle):
    print "SetServo = " + str(angle)


#parse connectionstring
try:
    opts, args = getopt.getopt(argv, "d:h:k:")
except getopt.GetoptError:
    print 'Usage: -d <deviceId> -h <hostname> -k <sharedkey>'
    sys.exit(2)

for opt,arg in opts:
    if opt == "-d":
        deviceId = arg
    elif opt == -"h":
        hostName = arg
    elif opt == "-k":
        sharedKey = arg

# set up azure connection
azure = AzureIOTHub(deviceId, hostName, sharedKey)

azure.registerCallBack(setServoCallBack, "SetServoAngle")
azure.hubConnect()
azure.updateDeviceState()

while True:
#	humidity, temperature = Adafruit_DHT.read_retry(dhtType, dhtPin)
	humidity = 75.2
	temperature = 26.0
	azure.sendMultipleSensorData({'Humidity':humidity, 'Temperature': temperature})
	time.sleep(2)
	azure.sendSensorData("Tilt", 0)
	time.sleep(2)
	azure.simulateCallBack("SetServoAngle", 27)
        time.sleep(2)



