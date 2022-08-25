phrase = input("Type your input here: ")

if "Nemo" in phrase:
    nemo = phrase.index("Nemo")
    print(f"I found Nemo at index {nemo}")
else:
    print("I can't find Nemo :(")