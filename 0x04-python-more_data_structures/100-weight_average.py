#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_scores = list(map(lambda x: x[0] * x[1], my_list))
    total_w_scores = 0
    total_weight = 0

    for n in weighted_scores:
        total_w_scores += n
    for sample in my_list:
        total_weight += sample[1]
    w_av = total_w_scores / total_weight

    return (w_av)
