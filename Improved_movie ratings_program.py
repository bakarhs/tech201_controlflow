user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) < 117 and int(age) > 0:
        user_prompt = False

    else:
        print("Please enter your answer in digits and bellow 117. If your child is under 1 yrs old we advise we do not advise bringing them into the movie.")

if int(age) < 12:
    print('U and PG films are available')
elif int(age) < 15:
    print('U, PG and 12 films are available')
elif int(age) < 18:
    print("U, PG, 12 and 15 films are available")
else:
    print('all films are available')


