#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(max_num):
    """Generate a list of primes up to max_num using Sieve of Eratosthenes"""
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_num + 1, i):
                primes[multiple] = False
    return [i for i in range(2, max_num + 1) if primes[i]]


def isWinner(x, nums):
    """Determine the overall winner after x rounds of the Prime Game"""
    if not nums or x < 1:
        return None

    # Find the maximum number in nums
    max_n = max(nums)

    # Generate primes up to the maximum number in nums
    primes = sieve_of_eratosthenes(max_n)

    # Precompute wins for each round based on available primes
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(p <= n for p in primes)  # Count primes <= n

        # Maria wins if the count of primes is odd, Ben wins if it's even
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
