#!/usr/bin/env python

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = set(range(1, len(nums) + 1))
        for num in nums:
            missing.discard(num)
        return list(missing)

inputs = [[4,3,2,7,8,2,3,1], [1, 1], [2, 2]]
expecteds = [[5,6], [2], [1]]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.findDisappearedNumbers(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
