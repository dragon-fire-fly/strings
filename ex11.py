def dog_cat(phrase):
    if " dog " in phrase:
        phrase = phrase.replace(" dog ", " cat ")

    return(phrase)

print(dog_cat("A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."))

