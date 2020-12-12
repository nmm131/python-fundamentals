import random as m


def too_high_or_too_low_number_guessing_game():
    rand_num = m.randint(0, 100)
    user_guess = eval(input("Guess a number between 0 and 100: "))
    while user_guess != rand_num:
        if user_guess > rand_num:
            user_guess = eval(input("Too high. Try again: "))
            continue
        elif user_guess < rand_num:
            user_guess = eval(input("Too low. Try again: "))
            continue
    return "You guessed the correct number!"
