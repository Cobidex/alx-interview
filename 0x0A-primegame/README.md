# Prime Game
## Description
Maria and Ben are playing a game called Prime Game. In this game, they are given a set of consecutive integers starting from 1 up to and including n. They take turns choosing a prime number from the set and removing that number and its multiples from the set. The player who cannot make a move loses the game. Maria always goes first, and both players play optimally.

The task is to implement a function isWinner(x, nums) that determines the winner of each game given the number of rounds x and an array of nums representing n for each round. The function should return the name of the player who won the most rounds. If the winner cannot be determined, it should return None. The function should adhere to the following specifications:

Prototype: def isWinner(x, nums)
x is the number of rounds to be played
nums is an array of integers representing n for each round
The function should not import any external packages
The input values of n and x will not be larger than 10000
