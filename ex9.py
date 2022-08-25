def normalize(phrase):
    if phrase.upper() == phrase:
        print(f"{phrase.capitalize()}!")
    else:
        print(phrase)

normalize(input("Type your phrase here: "))