#!/usr/bin/env python

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        input_map = {
            'U': (0, 1),
            'D': (0, -1),
            'L': (-1, 0),
            'R': (1, 0),
        }
        x, y = (0, 0)
        for move in moves:
            dx, dy = input_map[move]
            x += dx
            y += dy
        return x == 0 and y == 0


inputs = ['UD', 'LL']
expecteds = [True, False]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.judgeCircle(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
