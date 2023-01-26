import modules.alphabetconverter as alphcon

# Globals
port = 18
unit = 0.5
on = True
off = False

ac = alphcon.AlphabetConverter(port, unit)

ac.word_space()
ac.s()
ac.letter_space()
ac.t()
ac.letter_space()
ac.u()

