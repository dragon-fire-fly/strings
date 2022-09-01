
given_string = """One morning, when Gregor Samsa woke from troubled dreams, 
he found himself transformed in his bed into a horrible vermin.
 He lay on his armour-like back, and if he lifted his head a 
little he could see his brown belly, slightly domed and divided by 
arches into stiff sections. The bedding was hardly able to cover 
it and seemed ready to slide off any moment. His many legs, pitifully 
thin compared with the size of the rest of him, waved about helplessly 
as he looked."""

# hello = (given_string[68] + given_string[216:219] + given_string[5]).capitalize()
# gregor = given_string[18:24]
# print(hello, gregor)


## Waheed's answer:

# ns = len(given_string)

def select_word(word, given_string):
    greet = word
    # ng = len(greet)
    greet_new=""
    num1 = ""
    for char1 in greet:
        for char2 in given_string:
            if char2==char1:
                greet_new += char2
                num=given_string.index(char2)
        num1 += given_string[num]
        print(f"{given_string[num] :>10}    [{num:2}]")
    return num1

word1 = input("input seach word: ")
word2 = input("input seach word: ")

string1 = select_word(word1, given_string)

string2 = select_word(word2, given_string)

print(f"   {string1} {string2}")