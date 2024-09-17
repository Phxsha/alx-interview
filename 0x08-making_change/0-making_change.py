#!/usr/bin/python3
"""0-make_changes"""
import sys


def makeChange(coins, total):
    """ Deteremines fewest number of coins needed """
    if total <= 0:
        return 0

    # Initialize the dp array with a large value representing infinity
    dp = [sys.maxsize] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make a total of 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != sys.maxsize else -1
