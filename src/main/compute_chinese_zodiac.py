def compute_chinese_zodiac(year):
    if year % 12 == 0:
        return "Monkey"
    elif year % 12 == 1:
        return "Rooster"
    elif year % 12 == 2:
        return "Dog"
    elif year % 12 == 3:
        return "Pig"
    elif year % 12 == 4:
        return "Rat"
    elif year % 12 == 5:
        return "Ox"
    elif year % 12 == 6:
        return "Tiger"
    elif year % 12 == 7:
        return "Rabbit"
    elif year % 12 == 8:
        return "Dragon"
    elif year % 12 == 9:
        return "Snake"
    elif year % 12 == 10:
        return "Horse"
    elif year % 12 == 11:
        return "Sheep"