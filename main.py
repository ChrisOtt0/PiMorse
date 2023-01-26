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

    if com == "1":
        ac.one()
    elif com == "2":
        ac.two()
    elif com == "3":
        ac.three()
    elif com == "4":
        ac.four()
    elif com == "5":
        ac.five()
    elif com == "6":
        ac.six()
    elif com == "7":
        ac.seven()
    elif com == "8":
        ac.eight()
    elif com == "9":
        ac.nine()
    elif com == "0":
        ac.zero()
    else:
        print("Unknown number.")
