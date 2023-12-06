#!/usr/bin/python3
def complex_delete(a_dict, value):
    tmp = a_dict.copy()
    for k, v in tmp.items():
        if value == v:
            a_dict.pop(k)
            return a_dict
