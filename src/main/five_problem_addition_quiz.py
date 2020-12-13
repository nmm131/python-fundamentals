import random as m


def five_problem_addition_quiz():
    count = 0
    correct_count = 0

    while count < 5:
        rand_num_1 = m.randint(1, 10)
        rand_num_2 = m.randint(1, 10)
        user_answer = eval(input("What is {} + {} \n".format(rand_num_1, rand_num_2)))
        is_answer_correct = bool(int(user_answer) == (rand_num_1 + rand_num_2))
        if is_answer_correct:
            correct_count += 1
        count += 1

    return correct_count
