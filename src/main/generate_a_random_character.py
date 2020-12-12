import random as m


def generate_a_random_character():
    ch1 = 'a'
    ch2 = 'z'
    return chr(m.randint(ord(ch1), ord(ch2)))
