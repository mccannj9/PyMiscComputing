#! /usr/bin/env python


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
    original = set(numbers)
    complement = set()
    for addend in original:
        complement.add(value-addend)
    return 0




def main():
    print(find_sum_quadratic(7, [1,2,3,4]))


if __name__ == '__main__':
    main()
