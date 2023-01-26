import modules.alphabetconverter as alphcon

# Globals
port = 18
unit = 0.5
on = True
off = False

ac = alphcon.AlphabetConverter(port, unit)

ac.word_space()
ac.a()
ac.inletter_space()
ac.b()
ac.inletter_space()
ac.c()

