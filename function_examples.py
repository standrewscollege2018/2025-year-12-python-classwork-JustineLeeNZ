''' example of using functions - Justine Lee'''

# function definitions
def say_hello_world():
    print("Hello world!")
    print("Hello again")

# function with one parameter
def say_hello_name(my_name):
    print(my_name)


# function with 2 parameters
def display_student_info(name, age):
    print(f"Student name: {name}. Student age:{age}")

# function with return value
def add_values(num1, num2):
    result = num1 + num2

    return result

# function with Boolean return value
def coolest_teacher(my_name):
    if my_name == "Mrs Lee":
        return True
    else:
        return False

# main program code
print("How to use functions")

say_hello_world()

say_hello_name("Thomas")
say_hello_name("Daisy")

# get user input to pass as parameter
student_name = input("Enter your name")
say_hello_name(student_name)

# test function with 2 parameters
student_age = int(input("Enter your age"))
display_student_info(student_name, student_age)


# test return value function
total_price = add_values(1,2)

# test functions with boolean return values
test_name = coolest_teacher("Mrs Lee")
print(test_name) # debug print

# use Boolean return value as variable
if test_name:
    print("Yay she's my favourite too")
else:
    print("sorry I don't agree")

# use Boolean return value in another test
if (coolest_teacher("Mr Adams")):
    print("Yay she's my favourite too")
else:
    print("sorry I don't agree")