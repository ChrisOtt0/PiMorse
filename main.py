import modules.alphabetconverter as alphcon

# Globals
port = 18
unit = 0.25
on = True
off = False

ac = alphcon.AlphabetConverter(port, unit)

while (True):
    com = raw_input("Input text: ")
    com = com.lower()
    ac.word_space()

    for x in com:
        if x == "a":
            ac.a()
        elif x == "b":
            ac.b()
        elif x == "c":
            ac.c()
        elif x == "d":
            ac.d()
        elif x == "e":
            ac.e()
        elif x == "f":
            ac.f()
        elif x == "g":
            ac.g()
        elif x == "h":
            ac.h()
        elif x == "i":
            ac.i()
        elif x == "j":
            ac.j()
        elif x == "k":
            ac.k()
        elif x == "l":
            ac.l()
        elif x == "m":
            ac.m()
        elif x == "n":
            ac.n()
        elif x == "o":
            ac.o()
        elif x == "p":
            ac.p()
        elif x == "q":
            ac.q()
        elif x == "r":
            ac.r()
        elif x == "s":
            ac.s()
        elif x == "t":
            ac.t()
        elif x == "u":
            ac.u()
        elif x == "v":
            ac.v()
        elif x == "w":
            ac.w()
        elif x == "x":
            ac.x()
        elif x == "y":
            ac.y()
        elif x == "z":
            ac.z()
        elif x == "1":
            ac.one()
        elif x == "2":
            ac.two()
        elif x == "3":
            ac.three()
        elif x == "4":
            ac.four()
        elif x == "5":
            ac.five()
        elif x == "6":
            ac.six()
        elif x == "7":
            ac.seven()
        elif x == "8":
            ac.eight()
        elif x == "9":
            ac.nine()
        elif x == "0":
            ac.zero()
        elif x == " ":
            ac.word_space()
        ac.letter_space()
