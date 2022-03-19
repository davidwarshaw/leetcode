#!/usr/bin/env python

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str(self.start) + ' - ' + str(self.end)

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        events = []
        for interval in intervals:
            events.append((interval.start, 'start'))
            events.append((interval.end, 'end'))
        events.sort()

        meetings = []
        max_meetings = 0
        for event in events:
            if event[1] == 'start':
                meetings.append(event)
                max_meetings = max(max_meetings, len(meetings))
            else:
                meetings.pop()

        return max_meetings


inputs = [[Interval(0, 30), Interval(5, 10), Interval(15, 20)],
          [Interval(7,10), Interval(2,4)],
          [Interval(0, 90), Interval(5, 80), Interval(10, 70)]]
expecteds = [2, 1, 3]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.minMeetingRooms(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
