# tech201_controlflow
tech201_controlflow

## Control flow
Control flow is the order in which individual statements, instructions, or function calls are executed or evaluated. The control flow of a Python program is regulated by conditional statements, loops, and function calls.

Control flow -> Flow through a particular decision process.

## If statement
Example of an if statement:
```
age = 19

if age >= 18:
    print("You are the correct age to watch this film and can buy a ticket")

if age < 18:
    print("I'm afraid you cannot watch thia movie, you are not old enough")
```
In an actual program there can be many if statements, so if they part of the same bulk of code we use elif and else to group these statements together.

## Elif and else

Example of using `elif` and `else`:
```
film_rating = "universal"

if film_rating.lower() == "universal":
    print("All age groups can watch this film")
elif film_rating.lower() == "pg":
    print("General viewing but parental guidance is advised")
elif film_rating.lower() == "12" or film_rating == "12a":
    print("12 rated movies may not be suitable for those under 12. supervision is recommended")
elif film_rating.lower() == 15:
    print("You must be 15 to watch 15 rated movies in the cinema")
elif film_rating.lower() == 18:
    print("You must be 18 to watch 18 rated movies in the cinema")
else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")
```

This shows how we can use `elif` and `else` in a if statement

Also in Python there aare no 'switch statements' or 'case statements'

# Looping
A For loop is where you define an iterator number and cycle through data (list/ dictioanry) 'foreach' entry in the data structure.

## Creating a for loop

```
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3],[4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for num in list_data:
    print(num * 2)
```

## Nested for loop

A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop"

Example of a nested for loop:
```
for data in embedded_lists:
    print (data)
    for num in data:
        print(num)
```

# Loops for dictionaries

Example of loops for a dictionary:
```
for item in dict_data.values:
    print(item)

for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)

for items in dict_data.values():
    print(items["money"])
```

You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.


## Loops and if statements

```
list_1 = [1, 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print("I found 3")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon")
```

# While loops

While loops monitor data rather than iterate. With the while loop we can execute a set of statements as long as a condition is true.

Example of a while loop:

```
x = 0

while x < 10:
    print(f"it's working -> {x}")
    x += 1 # incrementer
```
```
it's working -> 0
it's working -> 1
it's working -> 2
it's working -> 3
it's working -> 4
it's working -> 5
it's working -> 6
it's working -> 7
it's working -> 8
it's working -> 9
```

## Using break

The Python break statement immediately terminates a loop entirely. Program execution proceeds to the first statement following the loop body.

Example of using the `break` command:

```
while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x += 1

print(x) # x = 4
```

## Verify user input
The simplest way to accomplish this is to put the input method in a while loop.

Example of verifying user input:

```
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
```
