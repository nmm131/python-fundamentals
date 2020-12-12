def determine_divisibility_of_number_by_2_and_3(number):
    divisible_by_2 = number % 2 == 0
    divisible_by_3 = number % 3 == 0
    divisible_by_2_and_3 = divisible_by_2 and divisible_by_3
    if divisible_by_2_and_3:
        return "{} is divisible by 2 and 3".format(number)
    elif divisible_by_2:
        return "{} is divisible by 2".format(number)
    elif divisible_by_3:
        return "{} is divisible by 3".format(number)
    else:
        return "{} is not divisible by 2 or 3".format(number)
