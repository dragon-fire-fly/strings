################
#### Task 1 ####
################

city = "London"
print(city)

################
#### Task 2 ####
################
city = "berlin"
population = 3645000

print(f"{city.capitalize()}: {population}")

################
#### Task 3 ####
################

city = "london"
population = 900000

print(f"City: {city.capitalize()} ({city.isalpha()})")
print(f"Population: {population}")

################
#### Task 4 ####
################

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

print(f"capital: {text.index('capital')}")

################
#### Task 5 ####
################

text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
text_list = text.split()
print(text_list)


################
#### Task 6 ####
################

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

print(text.replace("capital", "capital of Germany"))