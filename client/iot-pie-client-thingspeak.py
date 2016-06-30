#!/usr/bin/env python
import Adafruit_DHT

import sys
import time
import argparse
import thingspeak

dhtType = 11
dhtPin = 17
channelId = ""
sharedKey = ""

#parse connectionstring
parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-c", "--channelId", type=str, help="Channel Id", required=True)
requiredNamed.add_argument("-k", "--sharedKey", type=str, help="Shared Accesss Key", required=True)
args = parser.parse_args()

# set up thingspeak channel
channel = thingspeak.Channel(id=args.channelId, write_key=args.sharedKey)


temperature = 0.0
humidity = 0.0

while True:
    humidity, temperature = Adafruit_DHT.read_retry(dhtType, dhtPin)
    channel.update({1:temperature, 2:humidity})
    print "Temp = " + str(temperature)
    time.sleep(15)



