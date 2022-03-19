#!/usr/bin/env python

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        transformed = []
        for row in A:
            row.reverse()
            inverted = [1 if e == 0 else 0 for e in row]
            transformed.append(inverted)
        return transformed


inputs = [[[1,1,0],[1,0,1],[0,0,0]],
          [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]]
expecteds = [[[1,0,0],[0,1,0],[1,1,1]],
             [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.flipAndInvertImage(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
