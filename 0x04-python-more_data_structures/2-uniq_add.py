#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_of_unique = 0
    unique_list = set(my_list)

    for i in unique_list:
        sum_of_unique += i

    return (sum_of_unique)
