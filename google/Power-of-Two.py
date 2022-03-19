#!/usr/bin/env python

import math

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return math.log2(n).is_integer() if n > 0 else False

inputs = [1, 16, 218, 0, -2]
expecteds = [True, True, False, False, False]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.isPowerOfTwo(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
