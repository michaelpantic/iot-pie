from PWMServo import PWMServo

servo = PWMServo()

servo.initHW()
servo.setValue(0)

raw_input(">")

servo.setValue(45)

raw_input(">")
servo.setValue(90)

raw_input(">")
servo.setValue(0)
raw_input(">")
