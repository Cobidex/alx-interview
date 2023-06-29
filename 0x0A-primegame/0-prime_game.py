#!/usr/bin/python3
'''
contains the isWinner function
'''


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= max_num:
        if primes[p]:
            for i in range(p * p, max_num + 1, p):
                primes[i] = False
        p += 1

    wins = {'Maria': 0, 'Ben': 0}

    for n in nums:
        count = sum(primes[2:n+1])
        if count % 2 == 0:
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Maria'] < wins['Ben']:
        return 'Ben'
    else:
        return None
