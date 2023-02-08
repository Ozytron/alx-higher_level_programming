#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for elem in row:
            if not type(elem) in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for elem in row:
            if not type(elem) in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    length = len(m_a[0])
    for i in range(len(m_a)):
        if len(m_a[i]) != length:
            raise TypeError("each row of m_a must be of the same size")

    length = len(m_b[0])
    for i in range(len(m_b)):
        if len(m_b[i]) != length:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")

    mul = []
    i = 0
    for row in m_a:
        value = 0
        j = 0
        mul_row = []
        while j < len(m_b[0]):
            value += (row[i] * m_b[i][j])
            if i == len(m_b) - 1:
                i = 0
                j += 1
                mul_row.append(value)
                value = 0
            else:
                i += 1
        mul.append(mul_row)
    return (mul)
