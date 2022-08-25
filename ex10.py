###1
def list_creator(tuple):
    shopping_list=", ".join(tuple)
    return shopping_list


print(list_creator(("bananas", "apples", "milk")))

### 2
def list_creator(*args):
    shopping_list = ""
    for item in args:
        shopping_list += f"{item}, "

    return shopping_list


print(list_creator("bananas", "apples", "milk"))