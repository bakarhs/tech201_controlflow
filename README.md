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





