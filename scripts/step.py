#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import math

CHANNEL1 = 7   #A_PHASE
CHANNEL2 = 11   #A_ENBLE
CHANNEL3 = 13   #B_PHASE
CHANNEL4 = 15   #B_ENBLE

CHANNEL5 = 31   #A_PHASE
CHANNEL6 = 33   #A_ENBLE
CHANNEL7 = 35   #B_PHASE
CHANNEL8 = 37   #B_ENBLE

WHEEL_SIZE = 53
WIDTH = 87

def init():
    channels = [CHANNEL1,CHANNEL2,CHANNEL3,CHANNEL4,CHANNEL5,CHANNEL6,CHANNEL7,CHANNEL8]
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channels, GPIO.OUT, initial=GPIO.HIGH)

def break_check(value, i, pattern):
    if (i + 1) * 4 >= value and (value % 4) == pattern:
        return 1
    else:
        return 0

def ahead(value):
    rpm = 30
    init()

    try:
        loop_amount = (value // 4) + 1
        for i in range(loop_amount):
            #print "1"
            # Acceleration control
            if loop_amount > 100:
                pulse_time = 60.0 / rpm / 200.0
                if i < 50:
                    rpm += 6
                if (loop_amount - i) < 50:
                    rpm -= 6
            elif loop_amount > 30:
                pulse_time = 60.0 / rpm / 200.0
                if i < 30:
                    rpm += 5
                if (loop_amount - i) < 30:
                    rpm -= 5
            else:
                pulse_time = 60.0 / rpm / 200.0
            GPIO.output(CHANNEL1, 1)
            GPIO.output(CHANNEL5, 1)
            GPIO.output(CHANNEL2, 0)
            GPIO.output(CHANNEL6, 0)
            GPIO.output(CHANNEL3, 1)
            GPIO.output(CHANNEL7, 1)
            GPIO.output(CHANNEL4, 0)
            GPIO.output(CHANNEL8, 0)
            time.sleep(pulse_time)
            if break_check(value, i, 1) == 1:
                GPIO.cleanup()
                break

            #print "2"
            GPIO.output(CHANNEL5, 0)
            GPIO.output(CHANNEL1, 1)
            GPIO.output(CHANNEL6, 1)
            GPIO.output(CHANNEL2, 0)
            GPIO.output(CHANNEL7, 1)
            GPIO.output(CHANNEL3, 0)
            GPIO.output(CHANNEL8, 0)
            GPIO.output(CHANNEL4, 1)
            time.sleep(pulse_time)
            if break_check(value, i, 2) == 1:
                GPIO.cleanup()
                break

            #print "3"
            GPIO.output(CHANNEL1, 0)
            GPIO.output(CHANNEL5, 0)
            GPIO.output(CHANNEL2, 1)
            GPIO.output(CHANNEL6, 1)
            GPIO.output(CHANNEL3, 0)
            GPIO.output(CHANNEL7, 0)
            GPIO.output(CHANNEL4, 1)
            GPIO.output(CHANNEL8, 1)
            time.sleep(pulse_time)
            if break_check(value, i, 3) == 1:
                GPIO.cleanup()
                break

            #print "4"
            GPIO.output(CHANNEL5, 1)
            GPIO.output(CHANNEL1, 0)
            GPIO.output(CHANNEL6, 0)
            GPIO.output(CHANNEL2, 1)
            GPIO.output(CHANNEL7, 0)
            GPIO.output(CHANNEL3, 1)
            GPIO.output(CHANNEL8, 1)
            GPIO.output(CHANNEL4, 0)
            time.sleep(pulse_time)
            if break_check(value, i, 0) == 1:
                GPIO.cleanup()
                break
            pass
    except KeyboardInterrupt:
        print "\nCtl+C"
        GPIO.cleanup()

def right(value):
    rpm = 30
    init()

    try:
        loop_amount = (value // 4) + 1
        pulse_time = 60.0 / rpm / 200.0

        for i in range(loop_amount):
            #print "1"
            GPIO.output(CHANNEL1, 1)
            GPIO.output(CHANNEL5, 1)
            GPIO.output(CHANNEL2, 0)
            GPIO.output(CHANNEL6, 0)
            GPIO.output(CHANNEL3, 1)
            GPIO.output(CHANNEL7, 1)
            GPIO.output(CHANNEL4, 0)
            GPIO.output(CHANNEL8, 0)
            time.sleep(pulse_time)
            if break_check(value, i, 1) == 1:
                GPIO.cleanup()
                break

            #print "2"
            GPIO.output(CHANNEL5, 1)
            GPIO.output(CHANNEL1, 1)
            GPIO.output(CHANNEL6, 0)
            GPIO.output(CHANNEL2, 0)
            GPIO.output(CHANNEL7, 0)
            GPIO.output(CHANNEL3, 0)
            GPIO.output(CHANNEL8, 1)
            GPIO.output(CHANNEL4, 1)
            time.sleep(pulse_time)
            if break_check(value, i, 2) == 1:
                GPIO.cleanup()
                break

            #print "3"
            GPIO.output(CHANNEL1, 0)
            GPIO.output(CHANNEL5, 0)
            GPIO.output(CHANNEL2, 1)
            GPIO.output(CHANNEL6, 1)
            GPIO.output(CHANNEL7, 0)
            GPIO.output(CHANNEL3, 0)
            GPIO.output(CHANNEL4, 1)
            GPIO.output(CHANNEL8, 1)
            time.sleep(pulse_time)
            if break_check(value, i, 3) == 1:
                GPIO.cleanup()
                break

            #print "4"
            GPIO.output(CHANNEL5, 0)
            GPIO.output(CHANNEL1, 0)
            GPIO.output(CHANNEL6, 1)
            GPIO.output(CHANNEL2, 1)
            GPIO.output(CHANNEL7, 1)
            GPIO.output(CHANNEL3, 1)
            GPIO.output(CHANNEL8, 0)
            GPIO.output(CHANNEL4, 0)
            time.sleep(pulse_time)
            if break_check(value, i, 0) == 1:
                GPIO.cleanup()
                break
            pass
    except KeyboardInterrupt:
        print "\nCtl+C"
        GPIO.cleanup()

def left(value):
    rpm = 30
    init()

    try:
        loop_amount = (value // 4) + 1
        pulse_time = 60.0 / rpm / 200.0

        for i in range(loop_amount):
            #print "1"
            GPIO.output(CHANNEL1, 1)
            GPIO.output(CHANNEL5, 1)
            GPIO.output(CHANNEL2, 0)
            GPIO.output(CHANNEL6, 0)
            GPIO.output(CHANNEL3, 1)
            GPIO.output(CHANNEL7, 1)
            GPIO.output(CHANNEL4, 0)
            GPIO.output(CHANNEL8, 0)
            time.sleep(pulse_time)
            if break_check(value, i, 1) == 1:
                GPIO.cleanup()
                break

            #print "2"
            GPIO.output(CHANNEL5, 0)
            GPIO.output(CHANNEL1, 0)
            GPIO.output(CHANNEL6, 1)
            GPIO.output(CHANNEL2, 1)
            GPIO.output(CHANNEL7, 1)
            GPIO.output(CHANNEL3, 1)
            GPIO.output(CHANNEL8, 0)
            GPIO.output(CHANNEL4, 0)
            time.sleep(pulse_time)
            if break_check(value, i, 2) == 1:
                GPIO.cleanup()
                break

            #print "3"
            GPIO.output(CHANNEL1, 0)
            GPIO.output(CHANNEL5, 0)
            GPIO.output(CHANNEL2, 1)
            GPIO.output(CHANNEL6, 1)
            GPIO.output(CHANNEL3, 0)
            GPIO.output(CHANNEL7, 0)
            GPIO.output(CHANNEL4, 1)
            GPIO.output(CHANNEL8, 1)
            time.sleep(pulse_time)
            if break_check(value, i, 3) == 1:
                GPIO.cleanup()
                break

            #print "4"
            GPIO.output(CHANNEL5, 1)
            GPIO.output(CHANNEL1, 1)
            GPIO.output(CHANNEL6, 0)
            GPIO.output(CHANNEL2, 0)
            GPIO.output(CHANNEL7, 0)
            GPIO.output(CHANNEL3, 0)
            GPIO.output(CHANNEL8, 1)
            GPIO.output(CHANNEL4, 1)
            time.sleep(pulse_time)
            if break_check(value, i, 0) == 1:
                GPIO.cleanup()
                break
            pass
    except KeyboardInterrupt:
        print "\nCtl+C"
        GPIO.cleanup()

def main_loop(arg, value):
    if arg == 'a':
        value = int(float(value) / (float(WHEEL_SIZE) * math.pi / 200))
        ahead(value)
    if arg == 'r':
        value = int(float(WIDTH) * math.pi * float(value) / 360.0 / (float(WHEEL_SIZE) * math.pi / 200))
        right(value)
    if arg == 'l':
        value = int(float(WIDTH) * math.pi * float(value) / 360.0 / (float(WHEEL_SIZE) * math.pi / 200))
        left(value)
    pass

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 3:
        main_loop(args[1], args[2])
