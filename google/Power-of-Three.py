#!/usr/bin/env python

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0 and n % 3 == 0:
            n = n // 3
            if n == 1:
                return True
        return False if n != 1 else True

inputs = [27, 0, 9, 45, 1]
expecteds = [True, False, True, False, True]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.isPowerOfThree(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
