# def functionator_8000(word):
#     if word[-1] == "a" or word[-1] == "e" or word[-1] == "i" or word[-1] == "o" or word[-1] == "u":
#         print(f"{word.capitalize()}-inator {len(word)}000")
#     else:
#         print(f"{word.capitalize()}inator {len(word)}000")

# functionator_8000(input("Please choose a word: "))


#### Or 

# def functionator_8000(word):
#     if word[-1] in vowel_list:
#         print(f"{word.capitalize()}-inator {len(word)}000")
#     else:
#         print(f"{word.capitalize()}inator {len(word)}000")

# vowel_list = ["a", "e", "i", "o", "u"]
# functionator_8000(input("Please choose a word: "))

## Can also use "endswith()" method
## if word.endswith() ....
## endswith() method requires a string or tuple and does not work with a list


#### or

vowels = "aeiou"

def functionator_8000(word):
    if word[-1] in vowels:
        print(f"{word.capitalize()}-inator {len(word)}000")
    else:
        print(f"{word.capitalize()}inator {len(word)}000")

functionator_8000(input("Please choose a word: "))