#!/usr/bin/env python

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        heights = {}
        for person in people:
            height = person[0]
            if height not in heights:
                heights[height] = []
            heights[height].append(person)

        queue = [None] * len(people)
        for height in sorted(heights):
            k = 0
            for i in range(len(queue)):
                if not queue[i] or queue[i][0] >= height:
                    for person in heights[height]:
                        if person[1] == k:
                            queue[i] = person
                    k += 1

        return queue

inputs = [[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
          [[2, 4], [4, 1], [1, 6], [4, 2], [4, 0], [3, 1], [2, 2], [3, 2]],
          [[1, 1], [1, 0], [2, 1], [2, 0]],
          [[3, 0], [2, 0], [1, 0]],
          [[1, 1], [1, 0]],
          [[1, 0]]]
expecteds = [[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]],
          [[4, 0], [3, 1], [2, 2], [3, 2], [2, 4], [4, 1], [1, 6], [4, 2]],
          [[1, 0], [1, 1], [2, 0], [2, 1]],
          [[1, 0], [2, 0], [3, 0]],
          [[1, 0], [1, 1]],
          [[1, 0]]]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.reconstructQueue(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
