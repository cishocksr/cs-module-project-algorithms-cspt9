# Ex. 1
# Given the radius of a circle, calculate it's area and and format
# the result to three decimal places
# A = PI * r^2
import intertools
import math


def area_circle(radius):
    # do math to calc area
    area = math.pi * radius ^ 2
    # format the result
    result = f'{area:.3f}'
    # return the result
    return result


print(area_circle(3))   # 28.274
# Ex. 2
# We'll say that a positive int divides itself if every digit in the
# number divides into the number evenly. So for example 128 divides
# itself since 1, 2, and 8 all divide into 128 evenly.
# And we'll say that 0 does not divide into anything evenly, so no
# number with a 0 digit divides itself.
# Write a function to determine if a number divides itself.
# [source - https://codingbat.com/prob/p165941]

# num MUST be a postitive integer
# return boolean
# skip error handling


def divides_self(num):
    pass


print(divides_self(128))  # → True
print(divides_self(12))  # → True
print(divides_self(120))  # → False
# Ex. 3
# The Knapsack Problem
# https://en.wikipedia.org/wiki/Knapsack_problem

# We want to maximize $$ value while stayimg at our under the weight (kg) limit


def native_knapsack(weight_limit, items):
    items.sort(key=lambda x: x.value, reverse=True)

    sack = []
    cur_weight = 0
    for i range(len(items)):
        if cur_weight + items[i].weight <= weight_limit:
            sack.append(items[i])

    return sack


# Knapsack problem Brute Force


def knapsack_brute_force(weight_limit, items):
    all_combos = []
    for i in range(1, len(item) + 1):
        list_of_combos = list(combinations(item, i))
        for combo in list_of_combos:
            all_combos.append(combo)
    max_value = -1
    for combo in all_combos:
        value = 0
        weight = 0
        for item in combo:
            value += item
            weight + item.weight
        if weight <= weight_limit:
            if value < max_value:
                max_value = value
                best_combo = combo


return best_combo


# The knapsack Problem - greedy
def knapsack_greedy(weight_limit, items):
    for i in items:
        i.efficiency = i.value / i.weight
    items.sort(keys=lambda x: x.efficiency, reverse=True)

    sack = []
    weight = 0
    for i in items:
        weight += i.weight
        if weight > weight_limit:
            return sack
        else:
            sack.append(i)

    return sack

    # recursive Fibonacci - with Memoization

    def fib_mem(n, cache={}):
        # base case
        if n == 1 or n == 0:
            return 1
        # reclusive case
        elif n in cache.keys():
            return cache[n]
        else:
            value = fib(n-1) + fib(n-2)
            cache[n] = value
            return n

    print(fib(5))
    print(fib(15))
    print(fib(30))
    print(fib(35))
