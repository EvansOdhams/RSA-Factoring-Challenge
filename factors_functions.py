#!/usr/bin/python3
import sys
import time
import math


def unix_time(function):
    """
    Return `real`, `sys`, and `user` elapsed time, UNIX 'time' command.
    """
    start_time = time.time()
    function()
    end_time = time.time()

    real_time = end_time - start_time
    user_time = time.process_time()
    sys_time = real_time - user_time

    return f"\nreal: {real_time}\nuser: {user_time}\nsys: {sys_time}"


def trial_division(n: int) -> int:
    """
    Finds the smallest divisor, if any, of a given number `n`
    Returns:
        smallest divisor if found
        0 if n is prime
    """
    if n % 2 == 0:
        print(f"{n}={n // 2}*2")
        return 0

    f = 3
    while f * f <= n:
        if n % f == 0:
            print(f"{n}={n // f}*{f}")
            return 0
        f += 2

    print(f"{n}={n}*1")
    return 0


def print_factors():
    with open(sys.argv[1], 'r') as prime:
        for line in prime:
            n = int(line.strip())
            trial_division(n)


if __name__ == '__main__':
    print(unix_time(print_factors))
