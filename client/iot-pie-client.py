from AzureIOTHub import AzureIOTHub
#from PWMServo import PWMServo
import sys
#import Adafruit_DHT
import time

dhtType = 11
dhtPin = 17

def setServoCallBack(angle):
    print "SetServo = " + str(angle)

azure = AzureIOTHub('devid','host')

azure.registerCallBack(setServoCallBack, "SetServoAngle")

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



