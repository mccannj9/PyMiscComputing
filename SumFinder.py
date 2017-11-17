#! /usr/bin/env python


def time_it(f, *args):
    import time
    start = time.clock()
    f(*args)
    total_time = (time.clock() - start)*1000
    return "Process took %s milliseconds." % total_time


def find_sum_quadratic(value, numbers):

    """ quadratic solution to sum finder problem """
    print(value)
    for i in range(0, len(numbers)-1):
        x = numbers[i]

        for j in range(i+1, len(numbers)):
            y = numbers[j]

            if x + y == value:
                print((x, y))
                return x, y
    print(())
    return ()

def find_sum_linear(value, numbers):
    original = set(numbers)
    print(value)
    # complement = set()
    for addend in original:
        if value-addend in original:
            print((addend, value-addend))
            return (addend, value-addend)
    print(())
    return ()


def main():
    import random
    randints = [random.randint(0,2000000) for x in range(20000)]

    print(time_it(find_sum_quadratic, 2000000, randints))
    print(time_it(find_sum_linear, 2000000, randints))

    print(time_it(find_sum_quadratic, 7, [1,2,3,4]))
    print(time_it(find_sum_linear, 7, [1,2,3,4]))


if __name__ == '__main__':
    main()
