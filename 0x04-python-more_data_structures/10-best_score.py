#!/usr/bin.python3
def best_score(a_dictionary):
    if a_dictionary is not None and a_dictionary:
        key_value = sorted(a_dictionary, key=(lambda key: a_dictionary[key]))
        return key_value[-1]
    else:
        return None
