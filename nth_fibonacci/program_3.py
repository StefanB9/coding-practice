from timeit import timeit


def getNthFib(n):
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1] if n > 1 else last_two[0]


if __name__ == "__main__":
    print(timeit('getNthFib(18)', globals=globals(), number=100_000))
