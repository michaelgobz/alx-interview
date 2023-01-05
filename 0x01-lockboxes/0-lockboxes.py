#!usr/bin/python3
"""
The localboxes algorithm
"""


def canUnlockAll(boxes):
    """
    @params: boxes list of lists (set representation of boxes)
    Return: True if all can be opened and the reverse is true
    """
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
