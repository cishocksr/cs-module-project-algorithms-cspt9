#!/usr/bin/python

import sys


def making_change(amount, denominations):
    cache = [0 for _ in range(amount + 1)]
    cache[0] = 1

    for i in range(len(denominations)):
        for j in range(denominations[i], amount + 1):
            remainder = j - denominations[i]
            cache[j] += cache[remainder]

    return cache[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
