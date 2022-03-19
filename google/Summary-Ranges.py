#!/usr/bin/env python

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        prev = None
        range = []
        for num in nums:
            if prev is not None:
                if num - prev > 1:
                    ranges.append(range)
                    range = []
            range.append(num)
            prev = num
        else:
            ranges.append(range)

        range_summary = []
        for range in ranges:
            if len(range) > 1:
                range_summary.append(str(range[0]) + '->' + str(range[-1]))
            elif len(range) == 1:
                range_summary.append(str(range[0]))

        return range_summary


inputs = [[0, 1, 2, 4, 5, 7], [0, 2, 3, 4, 6, 8, 9], [1], [1, 10, 20], []]
expecteds = [["0->2", "4->5", "7"], ["0", "2->4", "6", "8->9"], ['1'], ['1', '10', '20'], []]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.summaryRanges(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
