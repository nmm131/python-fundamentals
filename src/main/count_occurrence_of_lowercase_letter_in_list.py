def count_occurrence_of_lowercase_letter_in_list(list_of_lowercase_letters, lowercase_letter):
    occurrence = 0

    for letter in list_of_lowercase_letters:
        if letter == lowercase_letter:
            occurrence += 1
    return occurrence
