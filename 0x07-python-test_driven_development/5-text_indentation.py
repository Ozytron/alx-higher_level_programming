#!/usr/bin/pyython3
def text_indentation(text):
    special_char = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] not in special_char:
            print(text[i], end='')
        else:
            print("{}\n".format(text[i]))
            if text[i + 1] == ' ':
                i += 1
        i += 1
