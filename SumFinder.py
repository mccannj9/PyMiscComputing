#! /usr/bin/env python


def time_it(f, *args):
    import time
    start = time.clock()
    f(*args)
    total_time = (time.clock() - start)*1000
    return "Process took %s milliseconds."


def find_sum_quadratic(value, numbers):

    """ quadratic solution to sum finder problem """
    
    for i in range(0, len(numbers)-1):
        x = numbers[i]
        
        for j in range(i+1, len(numbers)):
            y = numbers[j]

            if x + y == value:
                return x, y

    return -1

def find_sum_linear(value, numbers):
    complement = set()
    for addend in original:
        complement.add(value-addend)
    for addend in complement:
        if addend in original:
            return (addend, value-addend)
    return 0


def main():
    print(find_sum_quadratic(7, [1,2,3,4]))


if __name__ == '__main__':
    main()
