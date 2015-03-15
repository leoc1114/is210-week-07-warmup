#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""TASK 2"""


import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS[1] = ('Swan Lake')

BALLETS.append('Herman Schmerman')

BALLETS.extend(['Don Quixote', 'Sylvia'])
