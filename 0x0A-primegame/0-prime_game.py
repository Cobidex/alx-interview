#!/usr/bin/python3
"""
contains the prime game
"""


def isWinner(num_rounds, nums):
    """performs prime game"""
    if not nums or num_rounds < 1:
        return None

    max_num = max(nums)
    prime_filter = [True for _ in range(max(max_num + 1, 2))]
    prime_filter[0] = prime_filter[1] = False

    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if prime_filter[i]:
            for j in range(i * i, max_num + 1, i):
                prime_filter[j] = False

    primes_count = [0] * len(prime_filter)
    count = 0
    for i in range(len(prime_filter)):
        if prime_filter[i]:
            count += 1
        primes_count[i] = count

    player1_count = sum(primes_count[n] % 2 == 1 for n in nums)

    if player1_count * 2 == len(nums):
        return None
    if player1_count * 2 > len(nums):
        return "Maria"
    return "Ben"
