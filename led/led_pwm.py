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
    p = GPIO.PWM(PIN, 50)  # channel=12 frequency=50Hz
    p.start(0)
    try:
        while 1:
            print('up')
            for dc in range(0, 101, 5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
            print('down')
            for dc in range(100, -1, -5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
    except KeyboardInterrupt:
        p.stop()
        raise


try:
    setup()
    run()
except KeyboardInterrupt:
    cleanup()