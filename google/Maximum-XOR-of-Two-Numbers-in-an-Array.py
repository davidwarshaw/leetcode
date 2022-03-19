#!/usr/bin/env python

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = 0
        for num_a in nums:
            for num_b in nums:
                if num_a == num_b:
                    continue
                print(f"num_a: {num_a} num_b: {num_b} xor: {num_a ^ num_b}")
                max_xor = max(max_xor, num_a ^ num_b)
        return max_xor

inputs = [[3, 10, 5, 25, 2, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
expecteds = [28, 15]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.findMaximumXOR(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
