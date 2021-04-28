#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    num = 0
    for n in sys.argv:
        if i > 0:
            num += int(n)
        i += 1
    print(num)
