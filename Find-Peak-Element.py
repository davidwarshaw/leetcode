#!/usr/bin/env python

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bs(low, mid, high):
            # print()
            # print(f"{low} {mid} {high}")
            if abs(nums[high] - nums[low]) == abs(high - low):
                return high if nums[high] > nums[low] else low

            smaller_left = nums[mid - 1] < nums[mid] if mid - 1 >= 0 else True
            smaller_right = nums[mid + 1] < nums[mid] if mid + 1 < len(nums) else True
            if smaller_left and smaller_right:
                return mid

            # print(f"{abs(nums[mid] - nums[low])} < {abs(mid - low)}")
            # print(f"{low} + {(mid - low) // 2}")
            if abs(nums[mid] - nums[low]) <= abs(mid - low) or (abs(nums[mid] - nums[low]) == abs(mid - low) and smaller_right):
                return bs(low, low + ((mid - low) // 2), mid - 1)
            # print(f"{abs(nums[high] - nums[mid])} < {abs(high - mid)}")
            # print(f"{mid} + {(high - mid) // 2}")
            if abs(nums[high] - nums[mid]) <= abs(high - mid) or (abs(nums[high] - nums[mid]) == abs(high - mid) and smaller_left):
                return bs(mid + 1, mid + 1 + ((high - mid) // 2), high)

        return bs(0, len(nums) // 2, len(nums) - 1)

inputs = [[1, 2, 3, 1],
          [1, 2, 1, 3, 5, 6, 4],
          [3, 2, 1],
          [1, 2, 3],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
          [1, 2],
          [1],
          [1, 2, 3, 4, 3],
          [1, 6, 5, 4, 3, 2, 1],
          [1, 2, 3, 4, 5, 6, 1],
          [2, 1, 2],
          [1, 2, 5, 4, 3, 2, 1]]
expecteds = [2, 1, 0, 2, 10, 1, 0, 3, 1, 5, 2, 2]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.findPeakElement(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
