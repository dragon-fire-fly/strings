import datetime

def normalize(phrase):
    today = datetime.datetime.today().strftime("%d-%m") 
    if str(today) == "22-10":
        print("Happy CAPS LOCK DAY")
        print(phrase)
    else:
        if phrase.upper() == phrase:
            print("Dude, CAPS LOCK DAY is over!")
            print(f"{phrase.capitalize()}!")
        else:
            print(phrase.capitalize())

normalize(input("Type your phrase here: "))


### without datetime:

# def normalize(phrase):
#     if phrase.upper() == phrase:
#         print("Dude, CAPS LOCK DAY is over!")
#         print(f"{phrase.capitalize()}!")
#     else:
#         print(phrase.capitalize())

# normalize(input("Type your phrase here: "))