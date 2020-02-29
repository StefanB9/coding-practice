from timeit import timeit


def getNthFib(n, memoize=None):
    if memoize is None:
        memoize = {1: 0, 2: 1}
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        return memoize[n]


if __name__ == "__main__":
    print(timeit('getNthFib(18)', globals=globals(), number=100_000))
