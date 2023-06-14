#!/usr/bin/python3
""" contains the makeChange function """
from typing import List, Dict


def recurseMakeChange(coins: List[int], utils: Dict) -> int:
    """ recursively determine fewest number of coins """
    if utils['index'] >= utils['length'] and utils['remainder'] > 0:
        return -1
    elif utils['index'] == utils['length']:
        return utils['numberCoins']
    elif coins[utils['index']] > utils['remainder']:
        utils['index'] += 1
        return recurseMakeChange(coins, utils)
    else:
        utils['numberCoins'] += utils['remainder'] // coins[utils['index']]
        utils['remainder'] = utils['remainder'] % coins[utils['index']]
        return recurseMakeChange(coins, utils)


def makeChange(coins: List[int], total: int) -> int:
    """determine fewest number of coin
    needed to meet a given amount
    """
    if total <= 0:
        return 0

    length: int = len(coins)
    coins.sort(reverse=True)
    utils: Dict = {
            'remainder': total,
            'length': length,
            'index': 0,
            'numberCoins': 0
            }

    return recurseMakeChange(coins, utils)
