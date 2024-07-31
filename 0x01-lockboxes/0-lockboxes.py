#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Parameters:
    boxes (list of list of int): Each box contains a list of keys to
    other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = set()
    stack = [0]  # Start with the first box

    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if key < n and key not in visited:
                    stack.append(key)

    return len(visited) == n
