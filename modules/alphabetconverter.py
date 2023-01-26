import time

def o(gpio, port, unit):
    i = 0
    while i < 3:
        dash(gpio, port, unit)
        inletter_space(unit)
        i += 1

def s(gpio, port, unit):
    i = 0
    while i < 3:
        dot(gpio, port, unit)
        inletter_space(unit)

def dot(gpio, port, unit):
    gpio.output(port, True)
    time.sleep(unit)
    gpio.output(port, False)

def dash(gpio, port, unit):
    gpio.output(port, True)
    time.sleep(3 * unit)
    gpio.output(port, False)

def inletter_space(unit):
    time.sleep(unit)

def letter_space(unit):
    time.sleep(2 * unit)

def word_space(unit):
    time.sleep(6 * unit)
