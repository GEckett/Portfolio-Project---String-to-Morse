from translator import Translator

on = True
t = Translator()

while on:
    phrase = input("What phrase do you want to translate into Morse?").upper()
    split = t.split_string(phrase)
    t.translate(split)
    again = input("Do you want to translate another phrase? Type Y to do another translation.").upper()
    if again == "Y":
        on = True
    else:
        on = False
