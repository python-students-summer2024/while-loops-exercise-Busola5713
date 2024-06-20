def get_starting_number():
        bottles = input("How many bottles of beer on the wall? ")
        if bottles >= "1":
            return int(bottles)

def sing(): 
    beer = get_starting_number()
    for i in range(beer, 0, -1):
        if i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.\nTake one down, pass it around, no more bottles of beer on the wall!\n")
        elif i == 2:
             print(f"{i} bottle of beer on the wall, {i} bottle of beer.\nTake one down, pass it around, {i-1} bottle of beer on the wall.\n")
        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down, pass it around, {i-1} bottles of beer on the wall.\n")
