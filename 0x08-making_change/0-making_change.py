#!/usr/bin/python3
"""Contains the make_change function"""
from typing import List, Dict


def recurse_make_change(coins: List[int], utils: Dict) -> int:
    """Recursively determine the fewest number of coins"""
    if utils['index'] >= utils['length'] and utils['remainder'] > 0:
        return -1
    elif utils['index'] == utils['length']:
        return utils['number_coins']
    elif coins[utils['index']] > utils['remainder']:
        utils['index'] += 1
        return recurse_make_change(coins, utils)
    else:
        utils['number_coins'] += utils['remainder'] // coins[utils['index']]
        utils['remainder'] = utils['remainder'] % coins[utils['index']]
        return recurse_make_change(coins, utils)


def make_change(coins: List[int], total: int) -> int:
    """Determine the fewest number of coins needed to meet a given amount"""
    if total <= 0:
        return 0

    length: int = len(coins)
    coins.sort(reverse=True)
    utils: Dict = {
        'remainder': total,
        'length': length,
        'index': 0,
        'number_coins': 0
    }

    return recurse_make_change(coins, utils)
