import random as m


def get_4_cards_randomly_from_a_deck_of_cards():
    deck = []
    four_random_cards_as_numbers = []
    four_random_cards_as_strings = []
    suit = ""
    number = None
    number_as_string = ""
    for card_number in range(52):
        deck.append(card_number)
    for count in range(4):
        random_number = deck[m.randint(1, 51)]
        four_random_cards_as_numbers.append(random_number)

        if four_random_cards_as_numbers[count] % 13 == 0:
            number = 1
        elif four_random_cards_as_numbers[count] % 13 == 1:
            number = 2
        elif four_random_cards_as_numbers[count] % 13 == 2:
            number = 3
        elif four_random_cards_as_numbers[count] % 13 == 3:
            number = 4
        elif four_random_cards_as_numbers[count] % 13 == 4:
            number = 5
        elif four_random_cards_as_numbers[count] % 13 == 5:
            number = 6
        elif four_random_cards_as_numbers[count] % 13 == 6:
            number = 7
        elif four_random_cards_as_numbers[count] % 13 == 7:
            number = 8
        elif four_random_cards_as_numbers[count] % 13 == 8:
            number = 9
        elif four_random_cards_as_numbers[count] % 13 == 9:
            number = 10
        elif four_random_cards_as_numbers[count] % 13 == 10:
            number = 11
        elif four_random_cards_as_numbers[count] % 13 == 11:
            number = 12

        if four_random_cards_as_numbers[count] // 13 == 0:
            suit = "Spades"
        elif four_random_cards_as_numbers[count] // 13 == 1:
            suit = "Hearts"
        elif four_random_cards_as_numbers[count] // 13 == 2:
            suit = "Diamonds"
        elif four_random_cards_as_numbers[count] // 13 == 3:
            suit = "Clubs"

        if number == 0:
            number_as_string = "Ace"
        elif number == 1:
            number_as_string = "2"
        elif number == 2:
            number_as_string = "3"
        elif number == 3:
            number_as_string = "4"
        elif number == 4:
            number_as_string = "5"
        elif number == 5:
            number_as_string = "6"
        elif number == 6:
            number_as_string = "7"
        elif number == 7:
            number_as_string = "8"
        elif number == 8:
            number_as_string = "9"
        elif number == 9:
            number_as_string = "Jack"
        elif number == 10:
            number_as_string = "Queen"
        elif number == 11:
            number_as_string = "King"

        four_random_cards_as_strings.append("{} of {}".format(number_as_string, suit))
    return four_random_cards_as_strings
