#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 4"""


def process_data(data):
    """Testing for loop.

    ARGS:
        data(mixed): a list or a tuple

    RETURNS:
        A total of all numbers & it's average.

    EXAMPLE:
        >>>process_data([1, 2, 3, 4])
        (10, 2.5)

    """
    total = sum(data)
    avg = total/float(len(data))
    return (total, avg)
