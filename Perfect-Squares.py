#!/usr/bin/env python

class Solution(object):

    def __init__(self):
        self.known_mins = {}

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def pick_next(left):
            min_count = left
            if left in self.known_mins:
                return self.known_mins[left]

            perfect_squares = []
            x = 2
            ps = x * x
            while ps <= left:
                perfect_squares.append(ps)
                x += 1
                ps = x * x
            perfect_squares.reverse()

            for ps in perfect_squares:
                count = 1 + pick_next(left - ps)
                if count < min_count:
                    min_count = count
                    self.known_mins[left] = min_count

            return min_count

        min_count = pick_next(n)

        return min_count


# 1, 4, 9, 16, 25
inputs = [12, 13, 18, 10, 16, 19, 23, 6175]
expecteds = [3, 2, 2, 2, 1, 3, 4, 4]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.numSquares(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
