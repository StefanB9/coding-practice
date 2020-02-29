from timeit import timeit


def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)


if __name__ == "__main__":
    print(timeit('getNthFib(18)', globals=globals(), number=10_000))
