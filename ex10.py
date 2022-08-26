# ### 1
# def join_list(shopping_list):
#     return ", ".join(shopping_list)


# print(join_list(["Juice", "Oats", "Apples", "Nuts"]))


# ### 2
# def list_creator(tuple):
#     shopping_list=", ".join(tuple)
#     return shopping_list


# print(list_creator(("bananas", "apples", "milk")))

# ### 3
# def list_creator(*args):
#     shopping_list = ""
#     for item in args:
#         shopping_list += f"{item}, "

#     return shopping_list

# print(list_creator("bananas", "apples", "milk"))


# more_items = True

# shopping_list = []
# item = input("What would you like to add to the shopping list?: ")
# shopping_list.append(item)
# print(shopping_list)

# while more_items:
#     more = input("Would you like to add another item? Y or N?: ")
#     if more == "N" or more =="n":
#         more_items = False
#     else:
#         item = input("What would you like to add to the shopping list?: ")
#         shopping_list.append(item)
#         print(shopping_list)   

# print("Your shopping list is:")
# print(", ".join(shopping_list))


## as a function:

def create_list(item):
    more_items = True
    shopping_list = []
    shopping_list.append(item)

    while more_items:
        more = input("Would you like to add another item? Y or N?: ")
        if more == "N" or more =="n":
            more_items = False
        else:
            item = input("What would you like to add to the shopping list?: ")
            shopping_list.append(item)
        final_list= ", ".join(shopping_list)

    return f"Your shopping list is: {final_list}"

print(create_list(input("What would you like to add to the shopping list?: ")))