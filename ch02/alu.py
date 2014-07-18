#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../ch01')

from gates import *

def HalfAdder(a, b):
    """HalfAdder:
       sum = LSB of a + b
       carry = MSB of a + b

    >>> HalfAdder(0, 0)
    [0, 0]
    >>> HalfAdder(0, 1)
    [1, 0]
    >>> HalfAdder(1, 0)
    [1, 0]
    >>> HalfAdder(1, 1)
    [0, 1]

|   a   |   b   |  sum  | carry |
|   0   |   0   |   0   |   0   |
|   0   |   1   |   1   |   0   |
|   1   |   0   |   1   |   0   |
|   1   |   1   |   0   |   1   |
    """

    sum = Xor(a, b)
    carry = And(a, b)
    return [sum, carry]

def FullAdder(a, b, c):
    """FullAdder:
       sum = LSB of a + b + c
       carry = MSB of a + b + c

    >>> FullAdder(0, 0, 0)
    [0, 0]
    >>> FullAdder(0, 0, 1)
    [1, 0]
    >>> FullAdder(0, 1, 0)
    [1, 0]
    >>> FullAdder(0, 1, 1)
    [0, 1]
    >>> FullAdder(1, 0, 0)
    [1, 0]
    >>> FullAdder(1, 0, 1)
    [0, 1]
    >>> FullAdder(1, 1, 0)
    [0, 1]
    >>> FullAdder(1, 1, 1)
    [1, 1]
    """

    s1, c1 = HalfAdder(a, b)
    sum, c2 = HalfAdder(s1, c)
    carry = Or(c1, c2)
    return [sum, carry]


if __name__ == '__main':
    import doctest
    doctest.testmod()