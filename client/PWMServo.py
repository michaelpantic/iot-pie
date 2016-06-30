import RPi.GPIO as GPIO
import time


class PWMServo:
    servoPin = 18
    pwm = None
    angle = 0

    def initHW(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servoPin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.servoPin, 50)
        self.angle = 0
        self.pwm.start(self.angle)
        
    def calcDutyCycle(self, angle):
        pulseWidth = float(angle)/180.0+1.0;
        return pulseWidth/20.0*100.0

    def getValue(self):
        return self.angle

    def setValue(self, angle):
        self.angle = self.calcDutyCycle(angle)
        self.pwm.ChangeDutyCycle(self.angle)
        time.sleep(0.1)
        self.pwm.ChangeDutyCycle(0)

    def stopHW(self):
        self.pwm.stop()

