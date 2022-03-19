#!/usr/bin/env python

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                max_j = i
                for j in range(i, len(nums)):
                    if nums[j] > nums[i]:
                        max_j = j

                temp = nums[max_j]
                nums[max_j] = nums[i]
                nums[i] = temp

                right_i = (len(nums) - (i + 1)) // 2
                #print(right_i)
                #right_i -= 0 if right_i % 2 == 0 or right_i == 1 else 1
                #print(right_i)

                for k in range(right_i):
                    #print()
                    #print(k)
                    left = i + 1 + k
                    right = len(nums) - 1 - k
                    #print(left)
                    #print(right)

                    temp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = temp

                break
        else:
            nums.sort()



inputs = [[1, 2, 3],
          [3, 2, 1],
          [1, 1, 5],
          [4, 3, 5, 1, 2],
          [2, 1, 5, 4, 3],
          [2, 1, 6, 5, 4, 3],
          [],
          [1, 3, 2],
          [2, 2, 7, 5, 4, 3, 2, 2, 1]]
expecteds = [[1, 3, 2],
             [1, 2, 3],
             [1, 5, 1],
             [4, 3, 5, 2, 1],
             [2, 3, 1, 4, 5],
             [2, 3, 1, 4, 5, 6],
             [],
             [2, 1, 3],
             [2, 3, 1, 2, 2, 2, 4, 5, 7]]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        print(f"input: {input}")
        print(f"expected: {expected}")
        s.nextPermutation(input)
        actual = input
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
