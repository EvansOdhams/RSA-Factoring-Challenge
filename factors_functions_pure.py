#!/usr/bin/python3
import sys
import time


def trial_division(n: int) -> int:
    """
    Finds the smallest divisor, if any, of a given number `n`
    Returns:
        smallest divisor if found
        0 if n is prime
    """
    # TODO: Implement your own trial division function here
    pass


def print_factors():
    start_time = time.time()

    with open(sys.argv[1], 'r') as prime:
        for line in prime:
            n = int(line.strip())
            rep = trial_division(n)
            print("{}={}*{}".format(n, n // rep, rep))

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")


if __name__ == '__main__':
    print_factors()
