#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    count = len(sys.argv) - 1
    if count == 0:
        print('0 arguments.')
    elif count == 1:
        print('1 argument:')
    else:
        print('{:d} arguments:'.format(count))
    for s in sys.argv:
        if i > 0:
            print('{}: {}'.format(i, s))
        i += 1
