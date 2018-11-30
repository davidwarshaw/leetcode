#!/usr/bin/env python

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str(self.start) + '-' + str(self.end)

    def __repr__(self):
        return self.__str__()

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        bounds = []
        for interval in intervals:
            bounds.append((interval.start, 'start'))
            bounds.append((interval.end, 'end'))
        bounds.sort(key=lambda bound: bound[1], reverse=True)
        bounds.sort(key=lambda bound: bound[0], reverse=False)

        merged_start = None
        merge_stack = []
        merged = []
        for i, bound in enumerate(bounds):
            if bound[1] == 'start' and (i == 0 or bound[0] != bounds[i - 1][0] or bound[1] == bounds[i - 1][1]):
                if len(merge_stack) == 0:
                    merged_start = bound[0]
                merge_stack.append(bound)
            if bound[1] == 'end' and (i == len(bounds) - 1 or bound[0] != bounds[i + 1][0] or bound[1] == bounds[i + 1][1]):
                if len(merge_stack) == 1:
                    merged.append(Interval(merged_start, bound[0]))
                merge_stack.pop()

        return merged

inputs = [[Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)],
          [Interval(1, 4), Interval(4, 5)],
          [Interval(1, 4), Interval(1, 5)],
          [Interval(1, 5), Interval(2, 5)],
          [Interval(2, 3), Interval(0, 1), Interval(1, 2), Interval(3, 4), Interval(4, 5), Interval(1, 1), Interval(0, 1), Interval(4, 6), Interval(5, 7), Interval(1, 1), Interval(3, 5)]]
expecteds = [[Interval(1, 6), Interval(8, 10), Interval(15, 18)],
             [Interval(1, 5)],
             [Interval(1, 5)],
             [Interval(1, 5)],
             [Interval(0, 7)]]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.merge(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
