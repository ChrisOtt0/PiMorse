import modules.alphabetconverter as alphcon

# Globals
port = 18
unit = 0.5
on = True
off = False

ac = alphcon.AlphabetConverter(port, unit)

while (True):
    com = raw_input("Input number: ")
    ac.word_space()

    for x in com:
        if x == "1":
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
        else:
            print("Unknown number.")
