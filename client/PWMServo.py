import RPi.GPIO as GPIO
import time


class PWMServo:
	servoPin = 18
	pwm = None

	def initHW(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.servoPin, GPIO.OUT)
		self.pwm = GPIO.PWM(self.servoPin, 50)
		self.pwm.start(0)
		
	def calcDutyCycle(self, angle):
		pulseWidth = float(angle)/180.0+1.0;
		return pulseWidth/20.0*100.0


	def setValue(self, angle):
		self.pwm.ChangeDutyCycle(self.calcDutyCycle(angle))

	def stopHW(self):
		self.pwm.stop()

