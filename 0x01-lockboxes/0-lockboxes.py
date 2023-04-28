#!/usr/bin/python3
'''contains the unlockall method'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened'''
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)
    return all(visited)
