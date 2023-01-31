# While loops

# While loops monitor data rather than iterate

x = 0

# while x < 10:
#     print(f"it's working -> {x}")
#     x += 1 # incrementer

# it's working -> 0
# it's working -> 1
# it's working -> 2
# it's working -> 3
# it's working -> 4
# it's working -> 5
# it's working -> 6
# it's working -> 7
# it's working -> 8
# it's working -> 9

# Using break

# while x < 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break
#     x += 1

# print(x) # x = 4

# verify user input

# Asking for someone's age
# This can either be an int (20) or string (twenty)
# age = input("what is your name?")

# print(f"your age is {age}")

user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please enter your answer in digits and bellow 117")

print(f"Your age is {age}")



