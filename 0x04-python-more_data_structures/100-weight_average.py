#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_w_scores = 0
    total_weight = 0

    for sample in my_list:
        total_weight += sample[1]
        total_w_scores += (sample[0]*sample[1])

    return (total_w_scores / total_weight)
