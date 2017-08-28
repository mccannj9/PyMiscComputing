#! /usr/bin/env python


def make_change(change=0, coins=[]):
    """ 
        dynamic programming algorithm computing
        number of ways to make change from specified coins
        
    """

    # sets combos[0] = 1
    combos = [1] + [ 0 for x in range(1,change+1) ]

    for val in coins:
        for amount in range(1,change+1):
            print(combos)
            if amount >= val:
                combos[amount] += combos[amount-val]
        print("")

    print(combos)
    
    return combos[change]




def main():
    coins = [1,2,5]
    change = 12

    print(make_change(change, coins))

if __name__ == '__main__':
    main()
