#!/usr/bin/env python
from AzureIOTHub import AzureIOTHub
from PWMServo import PWMServo
import Adafruit_DHT

import sys
import time
import argparse

dhtType = 11
dhtPin = 17
deviceId = ""
hostName = ""
sharedKey = ""
servo = PWMServo()
servo.initHW()

def setServoCallBack(angle):
    global servo
    print "SetServo = " + str(angle)
    servo.setValue(angle)


#parse connectionstring
parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-d", "--deviceId", type=str, help="Device Id", required=True)
requiredNamed.add_argument("-n", "--hostName", type=str, help="Hostname of IOT Hub", required=True)
requiredNamed.add_argument("-k", "--sharedKey", type=str, help="Shared Accesss Key", required=True)
args = parser.parse_args()


# set up azure connection
azure = AzureIOTHub(args.deviceId, args.hostName, args.sharedKey)

azure.registerCallBack(setServoCallBack, "SetServoAngle")
azure.hubConnect()
azure.updateDeviceState()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(dhtType, dhtPin)
    azure.sendSensorData("Temperature", temperature)
    print "Temp = " + str(temperature)
    time.sleep(15)



