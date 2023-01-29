#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    if not a_dictionary:
        return (None)
    for key in a_dictionary:
        if a_dictionary[key] > score:
            score = a_dictionary[key]
            biggest_key = key

    return (biggest_key)
