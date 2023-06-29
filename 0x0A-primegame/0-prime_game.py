#!/usr/bin/python3
"""
contains the isWinner function
"""


def isWinner(num_rounds, nums):
    """function for the game"""
    if not nums or num_rounds < 1:
        return None
    max_num = max(nums)
    prime_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not prime_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            prime_filter[j] = False
    prime_filter[0] = prime_filter[1] = False
    primes_count = 0
    for i in range(len(prime_filter)):
        if prime_filter[i]:
            primes_count += 1
        prime_filter[i] = primes_count
    player1_count = 0
    for n in nums:
        player1_count += prime_filter[n] % 2 == 1
    if player1_count * 2 == len(nums):
        return None
    if player1_count * 2 > len(nums):
        return "Maria"
    return "Ben"
