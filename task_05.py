#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 5"""


def flip_keys(to_flip):
    """The list are reversed.

    ARGS:
        to_flip(mixed): a list of numbers or letters.

    RETURNS:
        A list of numbers or letters in reversed.

    EXAMPLES:
    >>> flip_keys(['day', 'night', (1, 2, 3)])
        ['yad', 'thgin', (3, 2, 1)]

    """
    counter = 0
    for values in to_flip:
        to_flip[counter] = values[::-1]
        counter += 1

    return to_flip
