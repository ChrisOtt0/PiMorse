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
        self.dash()

    def b(self):
        self.dash()
        for _ in range(3):
            self.dot()

    def c(self):
        for _ in range(2):
            self.dash()
            self.dot()

    def d(self):
        self.dash()
        for _ in range(2):
            self.dot()

    def e(self):
        self.dot()

    def f(self):
        for _ in range(2):
            self.dot()
        self.dash()
        self.dot()

    def g(self):
        for _ in range(2):
            self.dash()
        self.dot()

    def h(self):
        for _ in range(4):
            self.dot()

    def i(self):
        for _ in range(2):
            self.dot()

    def j(self):
        self.dot()
        for _ in range(3):
            self.dash()

    def k(self):
        self.dash()
        self.dot()
        self.dash()

    def l(self):
        self.dot()
        self.dash()
        for _ in range(2):
            self.dot()

    def m(self):
        for _ in range(2):
            self.dash()

    def n(self):
        self.dash()
        self.dot()

    def o(self):
        for _ in range(3):
            self.dash()

    def p(self):
        self.dot()
        for _ in range(2):
            self.dash()
        self.dot()

    def q(self):
        for _ in range(2):
            self.dash()
        self.dot()
        self.dash()

    def r(self):
        self.dot()
        self.dash()
        self.dot()

    def s(self):
        for _ in range(3):
            self.dot()

    def t(self):
        self.dash()

    def u(self):
        for _ in range(2):
            self.dot()
        self.dash()

    def v(self):
        for _ in range(3):
            self.dot()
        self.dash()

    def w(self):
        self.dot()
        for _ in range(2):
            self.dash()

    def x(self):
        self.dash()
        for _ in range(2):
            self.dot()
        self.dash()

    def y(self):
        self.dash()
        self.dot()
        for _ in range(2):
            self.dash()

    def z(self):
        for _ in range(2):
            self.dash()
        for _ in range(2):
            self.dot()

    def dot(self):
        self.gpio.output(self.port, True)
        time.sleep(self.unit)
        self.gpio.output(self.port, False)
        time.sleep(self.unit)

    def dash(self):
        self.gpio.output(self.port, True)
        time.sleep(3 * self.unit)
        self.gpio.output(self.port, False)
        time.sleep(self.unit)

    def letter_space(self):
        time.sleep(2 * self.unit)

    def word_space(self):
        time.sleep(6 * self.unit)
