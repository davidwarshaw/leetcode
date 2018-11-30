#!/usr/bin/env python

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        for i in range(0, len(nums), 2):
            if i < len(nums) - 1:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp

inputs = [[0],
          [1, 1, 1],
          [3, 5, 2, 1, 6, 4],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
expecteds = [[0],
             [1, 1, 1],
             [5, 6, 3, 4, 1, 2],
             [9, 10, 7, 8, 5, 6, 3, 4, 1, 2],
             [9, 10, 7, 8, 5, 6, 3, 4, 1, 2]]


if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        print(f"input: {input}")
        print(f"expected: {expected}")
        s.wiggleSort(input)
        print(f"actual: {input}")
        print(f"{input == expected}")
        print()
