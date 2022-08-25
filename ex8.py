
def find_nemo(phrase):
    if "Nemo" in phrase:
        nemo = phrase.index("Nemo")
        print(f"I found Nemo at index {nemo}")
    else:
        print("I can't find Nemo :(")

find_nemo(input("Type your input here: "))