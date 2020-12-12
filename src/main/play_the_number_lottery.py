import random as m

def play_the_number_lottery(two_digit_number):
    winning_number = m.randint(10, 99)
    number_matches_exact_order = two_digit_number == winning_number
    number_as_string = list(str(two_digit_number))
    number_digit_1 = eval(number_as_string[0])
    number_digit_2 = eval(number_as_string[1])
    winning_number_as_string = list(str(winning_number))
    winning_number_digit_1 = eval(winning_number_as_string[0])
    winning_number_digit_2 = eval(winning_number_as_string[1])
    number_matches_wrong_order = number_digit_1 + number_digit_2 == winning_number_digit_1 + winning_number_digit_2 and not number_matches_exact_order
    number_matches_one_digit = list(set(number_as_string).intersection(winning_number_as_string))

    if number_matches_exact_order:
        return 10000
    elif number_matches_wrong_order:
        return 3000
    elif number_matches_one_digit:
        return 1000
    else:
        return 0
