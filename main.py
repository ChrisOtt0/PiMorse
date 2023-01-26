import RPi.GPIO as GPIO
import modules.alphabetconverter as ac

# Globals
port = 18
unit = 1
on = True
off = False

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.OUT)

ac.word_space(unit)

ac.s(GPIO, port, unit)
