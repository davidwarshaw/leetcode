#!/usr/bin/env python

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        most = 0
        most_recent = 0

        while True:
            type_1 = -1
            type_2 = -1
            start = most_recent
            i = start

            while True:
                if (i == len(tree)) or (type_1 >= 0 and type_2 >= 0 and tree[i] != type_1 and tree[i] != type_2):
                    most = max(most, i - start)
                    break

                if type_1 < 0:
                    type_1 = tree[i]
                if type_2 < 0 and tree[i] != type_1:
                    type_2 = tree[i]

                if tree[i] == type_2 and tree[i - 1] != type_2:
                    most_recent = i

                i += 1

            if i == len(tree):
                break

        return most


inputs = [[1,2,1],
          [0,1,2,2],
          [1,2,3,2,2],
          [3,3,3,1,2,1,1,2,3,3,4],
          [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6],
          [0,1,6,6,4,4,6]]
expecteds = [3, 3, 4, 5, 11, 5]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.totalFruit(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
