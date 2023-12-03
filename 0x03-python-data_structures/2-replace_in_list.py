#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_len = len(my_list) -1
    if idx < 0 || idx > list_len:
        return None
    else:
        my_list[idx] = element
        return my_list
