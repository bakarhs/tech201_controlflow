import random

game_random_number = random.randint(1, 20)

print("Guess a number between 1-20")
for num in range(3):
    user_guess = int(input())
    if user_guess == game_random_number:
        print('You guess correctly')
        break
    elif user_guess < game_random_number:
        print("Too low, guess again")
    elif user_guess > game_random_number:
        print("Too high, guess again")
    elif num < 1 or num > 20:
        print("Your guess is not in range")
else:
    print(f"You didn't guess the right number. The answer was {game_random_number}")









