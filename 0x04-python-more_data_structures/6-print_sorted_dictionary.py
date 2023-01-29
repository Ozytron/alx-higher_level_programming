#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = list(a_dictionary.keys())
    key_list.sort()

    for k in key_list:
        print("{}: {}".format(k,a_dictionary.get(k)))
