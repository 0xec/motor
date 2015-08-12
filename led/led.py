import RPi.GPIO as GPIO
import time

PIN = 17

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    GPIO.setup(PIN, GPIO.OUT)

def cleanup():
    GPIO.cleanup()

def run():
    while True:
        print('close')
        GPIO.output(PIN, True)
        time.sleep(1)
        print('open')
        GPIO.output(PIN, False)
        time.sleep(1)

try:
    setup()
    run()
except KeyboardInterrupt:
    cleanup()