#! /usr/bin/env python


def find_sum_quadratic(value, numbers):

    """ quadratic solution to sum finder problem """
    for i in range(0, numbers):
        x = numbers[i]
        for j in range(1, numbers):
            y = numbers[j]

            if x + y == value:
                return x, y

    return -1


def main():
    pass


if __name__ == '__main__':
    main()
