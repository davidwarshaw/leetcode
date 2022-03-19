#!/usr/bin/env python

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0:
            return False
        elif len(matrix[0]) == 0:
            return False

        h = len(matrix)
        w = len(matrix[0])

        def bs(row, low, mid, high):
            #print(f"row: {row} low: {low} mid: {mid} high: {high}")
            if row[mid] == target:
                return True
            if high - low == 1:
                return high
            if target < row[mid]:
                return bs(row, low, low + ((mid - low) // 2), mid)
            if target > row[mid]:
                return bs(row, mid, mid + ((high - mid) // 2), high)

        high_constraint = w
        for row in matrix:
            rs = bs(row, 0, high_constraint // 2, high_constraint)
            if rs is True:
                return rs
            else:
                #print(f"high_constraint: {high_constraint}")
                high_constraint = rs

        return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
inputs = [5, 20, 24, 1, 11, 13, 31, 18]
expecteds = [True, False, True, True, True, True, False, True]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.searchMatrix(matrix, input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
