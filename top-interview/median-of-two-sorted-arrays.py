#!/usr/bin/env python

from typing import List

from math import floor

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_len = len(nums1) + len(nums2)
        odd = nums_len % 2 == 1
        stop_i = floor(nums_len / 2) if odd else int((nums_len / 2) - 1)

        i = 0
        i1 = 0
        i2 = 0
        current = None
        answer = None
        while True:
            if i1 < len(nums1) and (i2 >= len(nums2) or nums1[i1] <= nums2[i2]):
                current = nums1[i1]
                i1 += 1
            elif i2 < len(nums2) and (i1 >= len(nums1) or nums2[i2] <= nums1[i1]):
                current = nums2[i2]
                i2 += 1
            else:
                break

            print(f"i: {i} i1: {i1} i2: {i2} -> current: {current}")

            if i == stop_i or i == stop_i + 1:
                if answer:
                    answer = (answer + current) / 2
                    break

                if odd:
                    answer = float(current)
                    break
                else:
                    answer = current

            i += 1

        return answer


inputs = [([1, 3], [2]), ([1, 2], [3, 4]), ([1], [1]), ([2, 3], [2])]
expecteds = [2.0, 2.5, 1.0, 2.0]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.findMedianSortedArrays(input[0], input[1])
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
