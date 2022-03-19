#!/usr/bin/env python

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            l = nums[i]
            for j in range(i + 1, len(nums), 1):
                r = nums[j]
                # print(f"{i}, {j} -> {l}, {r}")
                if l + r == target:
                    return i, j
            # print()

inputs = [[[2, 7, 11, 15], 9]]
expecteds = [[0, 1]]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.twoSum(input[0], input[1])
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
