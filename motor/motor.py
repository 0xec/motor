#!/usr/bin/env python
#-*-coding:utf8-*-
import time
try:
    import RPi.GPIO as GPIO
except:
    pass


IN1 = 5  # pin11
IN2 = 6
IN3 = 13
IN4 = 19

PINS = [5, 6, 13, 19]

Code_CCW = [0x08, 0x0c, 0x04, 0x06, 0x02, 0x03, 0x01, 0x09]
Code_CW_ = [0x09, 0x01, 0x03, 0x02, 0x06, 0x04, 0x0c, 0x08]

def setStep(bCode):
    bCode = bCode & 0x0f
    for idx in range(0, 4):
        ch = (bCode & 0x08) >> 3 ^ 1
        # print('%1u' % ch),
        bCode = bCode << 1
        GPIO.output(PINS[3-idx], ch)

    # print('')



def stop():
    setStep(1)


def forward(delay, steps):
    for i in range(0, steps):
        for idx in Code_CW_:
            setStep(idx)
            time.sleep(delay)

def backward(delay, steps):
    for i in range(0, steps):
        for idx in Code_CCW:
            setStep(idx)
            time.sleep(delay)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, 1)
    GPIO.setup(IN1, GPIO.OUT)  # Set pin's mode is output
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)


def loop():
    while True:
        print('forward...')
        forward(0.03, 100)
        stop()
        time.sleep(1)
        
        print("backward...")
        backward(0.03, 100)  # 512 steps --- 360 angle
        stop()
        time.sleep(1)
        

def destroy():
    GPIO.cleanup()  # Release resource

# for idx in Code_CCW:
#     setStep(idx)
#     #time.sleep(delay)
if __name__ == '__main__':  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
        destroy()
