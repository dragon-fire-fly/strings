################
#### Task 1 ####
################

text = "Berlin is a world city of culture, politics, media and science."

print(len(text))

################
#### Task 2 ####
################

print(text[0], text[-1])

################
#### Task 3 ####
################

print(text[:3].upper())

################
#### Task 4 ####
################

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"

print(f"B appears {text.count('B')} times")

################
#### Task 5 ####
################

text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

print(f"Last ten characters: {text[-10:]}")

################
#### Task 6 ####
################

text = "---Python programming---"

print(text.strip("-"))

################
#### Task 7 ####
################

first = "Emily"
last = "Knight"

print(f"Firstname: {first} \nLastname: {last}")
