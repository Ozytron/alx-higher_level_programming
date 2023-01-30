#!/usr/bin/python3
def subtract_roman(list_numbers):
    num_to_subtract = 0
    max_num_list = max(list_numbers)

    for num in list_numbers:
        if num < max_num_list:
            num_to_subtract += num

    return (max_num_list - num_to_subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    number = 0
    last_num = 0
    list_numbers = [0]

    rom_id = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    key_list = list(rom_id.keys())

    for symbol in roman_string:
        for rom_num in key_list:
            if rom_num == symbol:
                if rom_id.get(symbol) <= last_num:
                    number += subtract_roman(list_numbers)
                    list_numbers = [rom_id.get(symbol)]
                else:
                    list_numbers.append(rom_id.get(symbol))
                last_num = rom_id.get(symbol)

    number += subtract_roman(list_numbers)
    return (number)
