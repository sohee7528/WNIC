import RPi.GPIO as GPIO
import time
buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setwarnings(False)

pwn=GPIO.PWM(buzzer, 262)
pwn.start(50.0)
time.sleep(1.5)

pwn.stop()
GPIO.cleanup()
