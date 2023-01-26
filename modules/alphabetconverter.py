import RPi.GPIO as GPIO
import time

class AlphabetConverter:
    gpio = GPIO
    def __init__(self, port, unit):
        self.port = port
        self.unit = unit
        self.gpio.setmode(GPIO.BCM)
        self.gpio.setup(port, GPIO.OUT)

    def a(self):
        self.dot()
        self.inletter_space()
        self.dash()
        self.inletter_space()

    def b(self):
        self.dash()
        self.inletter_space()
        i = 0
        while i < 3:
            self.dot()
            self.inletter_space()
            i += 1

    def c(self):
        i = 0
        while i < 2:
            self.dash()
            self.inletter_space()
            self.dot()
            self.inletter_space()
            i += 1

    def o(self):
        i = 0
        while i < 3:
            self.dash()
            self.inletter_space()
            i += 1

    def s(self):
        i = 0
        while i < 3:
            self.dot()
            self.inletter_space()
            i += 1

    def dot(self):
        self.gpio.output(self.port, True)
        time.sleep(self.unit)
        self.gpio.output(self.port, False)

    def dash(self):
        self.gpio.output(self.port, True)
        time.sleep(3 * self.unit)
        self.gpio.output(self.port, False)

    def inletter_space(self):
        time.sleep(self.unit)

    def letter_space(self):
        time.sleep(2 * self.unit)

    def word_space(self):
        time.sleep(6 * self.unit)
