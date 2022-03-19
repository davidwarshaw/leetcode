#!/usr/bin/env python

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def _pow(x, n):
            if n == 0:
                return 1.0
            elif n < 0:
                return 1 / _pow(x, -n)
            elif n % 2 > 0:
                return _pow(x * x, n // 2) * x
            else:
                return _pow(x * x, n // 2)

        return round(_pow(x, n), 10)

inputs = [[2.00000, 10], [2.10000, 3], [2.00000, -2], [0.00001, 2147483647], [0, 1], [1, 0]]
expecteds = [1024.00000, 9.26100, 0.25000, 0, 0, 1]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.myPow(input[0], input[1])
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
