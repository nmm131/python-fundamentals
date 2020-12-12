import random as m


def addition_quiz():
    rand_num_1 = m.randint(1, 10)
    rand_num_2 = m.randint(1, 10)
    user_answer = eval(input("What is {} + {} \n".format(rand_num_1, rand_num_2)))
    is_answer_correct = bool(user_answer == (rand_num_1 + rand_num_2))

    return is_answer_correct
