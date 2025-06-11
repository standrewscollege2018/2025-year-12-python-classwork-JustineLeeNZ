''' lists and dictionaries - Justine Lee'''

# ***** Lists *****
# example list of food names

# simple list
foods = ["chocolate","cheese","banana"]

# testing in function with a simple list - it works :-)
if "cheese" in foods:
    print("Found food")
else:
    print("Food not found")

# example list of lists storing favourite colours
favourite_colours = [["Hannah","pink"], ["Cameron","blue"], ["Josh","lemon chiffon"]]

# testing in function with a list of lists - DOESN'T work nicely :-(
if "pink" in favourite_colours:
    print("Found colour")
else:
    print("Colour not found")

# printing the list using range in for loop - to get numbered list
print("Naughty list")
for i in range(0,len(favourite_colours)):
    print(f"{i+1} {favourite_colours[i]}")

# printing the list using CONDENSED for loop - coz don't need numbered list
for colour in favourite_colours:
    print(colour)

# ***** - Dictionaries *****
my_dictionary = {
        "Cohnor" : "black",
        "Josh" : "lemon chiffon",
        "Alex" : "dark goldenrod",
        "Daisy" : 5
    }
# access individual item from dictionary
print(f"Student's fav colour is {my_dictionary['Josh']}")

# add item to dictionary
my_dictionary['Thomas'] = "lime green"

# show that item is now in dictionary
print(f"Thomas' fav colour is {my_dictionary['Thomas']}")

# ugly print dictionary for debugging
print(my_dictionary)

# all values in dictionary, nicely formatted
print("=========================")
for name,colour in my_dictionary.items():
    print(f"{name}'s fav colour is {colour}")

# update value
my_dictionary["Daisy"] = my_dictionary["Daisy"] + 10

# check that value has updated - it has :-)
print(my_dictionary["Daisy"])


