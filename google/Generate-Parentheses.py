#!/usr/bin/env python

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        lines = []
        def fill(lefts, rights, line, parens):
            if parens == 2 * n:
                if lefts == rights:
                    lines.append(line)
                return
            fill(lefts + 1, rights, line + '(', parens + 1)
            if lefts > rights:
                fill(lefts, rights + 1, line + ')', parens + 1)

        fill(0, 0, '', 0)
        return lines

inputs = [3, 2]
expecteds = [["((()))",
              "(()())",
              "(())()",
              "()(())",
              "()()()"],
             ["(())",
              "()()"]]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.generateParenthesis(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
