#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        tup_list = [len(sentence), sentence[0]]
    else:
        tup_list = [len(sentence), None]
    return tuple(tup_list)
