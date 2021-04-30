#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    temp = 0
    num = 0
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for ele in roman_string:
        if temp == 0:
            num += int(rom.get(ele))
        elif temp < int(rom.get(ele)) and temp != 0:
            num += ((int(rom.get(ele)) - temp) - temp)
        elif temp >= int(rom.get(ele)) and temp != 0:
            num += int(rom.get(ele))
        temp += int(rom.get(ele))
    return num
