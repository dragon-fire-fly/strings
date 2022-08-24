#####################
#### Secret Love ####
#####################

secret = input("Secret: ")
name = input("Name: ")
year = input("Year: ")

while len(secret)<9:
    print("Your secret must be at least 8 characters long. Please try again.")
    secret = input("Secret: ")

secret_name = secret + name
reversed = secret_name[::-1]
with_year = reversed + str(year)

print(with_year)