import RPi.GPIO as GPIO
from picamera import PiCamera

switch=16

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, GPIO.PUD_DOWN)

camera = PiCamera()
camera.start_preview()

try:
    while 1:
        if GPIO.input(switch) == 1:
            camera.capture('/home/pi/capture.jpg')
except KeyboardInterrupt:
    GPIO.cleanup()
    camera.stop_preview()
