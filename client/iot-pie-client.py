from AzureIOTHub import AzureIOTHub
from PWMServo import PWMServo
import sys
import Adafruit_DHT
import time

dhtType = 11
dhtPin = 17


azure = AzureIOTHub('devid','host')


while True:
	humidity, temperature = Adafruit_DHT.read_retry(dhtType, dhtPin)
	azure.sendSensorData({'Humidity':humidity, 'Temperature': temperature})
	time.sleep(5)

