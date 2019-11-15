#!/usr/bin/env python
import RPi.GPIO as gpio
import time

RESET_PIN = 18 

gpio.setmode(gpio.BCM)
gpio.setup(RESET_PIN, gpio.OUT)

# reset is pulled low
gpio.output(RESET_PIN, 0)
time.sleep(0.5)
gpio.output(RESET_PIN, 1)
print("reset rotator controller")

gpio.cleanup()
