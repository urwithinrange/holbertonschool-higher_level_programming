#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tup_list = [len(sentence), None]
    else:
        tup_list = [len(sentence), sentence[0]]
    return tuple(tup_list)
