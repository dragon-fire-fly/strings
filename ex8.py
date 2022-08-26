
def find_nemo(phrase: str) -> str:
    if "Nemo" in phrase:
        nemo = phrase.index("Nemo")
        return f"I found Nemo at index {nemo}"
    elif "nemo" in phrase:
        nemo = phrase.index("nemo")
        return f"I found Nemo at index {nemo}"
    else:
        return "I can't find Nemo :("

print(find_nemo(input("Type your input here: ")))





# ### Simplified

# phrase = input("Type your input here: ")
# if "Nemo" in phrase:
#     nemo = phrase.index("Nemo")
#     print(f"I found Nemo at index {nemo}")
# else:
#     print("I can't find Nemo :(")