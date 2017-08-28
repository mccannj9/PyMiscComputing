#! /usr/bin/env python


class Memoize(object):
    """docstring for Memoize"""
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        ret = self.func(*args)
        self.cache[args] = ret
        return ret
        

@Memoize
def dynamic_fib(term):
    if term < 2:
        return 1

    return dynamic_fib(term - 2) + dynamic_fib(term - 1)


def recursive_fib(term):
    if term < 2:
        return term

    return recursive_fib(term - 1) + recursive_fib(term - 2)


def iterative_fib(term):
    if term < 2:
        return term

    fib = [0,1]
    for x in range(2, term + 1):
        fib.append(fib[x - 1] + fib[x - 2])
    return fib[term]


def main():

    for x in range(0, 10):
        u = recursive_fib(x)
        v = iterative_fib(x)
        w = dynamic_fib(x-1)

        print("rec = %s ::: iter = %s ::: dyn = %s" % (u,v,w))


if __name__ == '__main__':
    main()
