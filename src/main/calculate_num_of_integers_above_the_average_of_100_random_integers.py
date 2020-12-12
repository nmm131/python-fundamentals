import random as m


def calculate_num_of_integers_above_the_average_of_100_random_integers():
    one_hundred_random_integers = []
    number_integers_above_average = 0
    for count in range(1, 101):
        random_integer = m.randint(1, 100)
        one_hundred_random_integers.append(random_integer)
    one_hundred_random_integers_average = sum(one_hundred_random_integers) / 100
    for num in one_hundred_random_integers:
        if num > one_hundred_random_integers_average:
            number_integers_above_average += 1
    return number_integers_above_average
