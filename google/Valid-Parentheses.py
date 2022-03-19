#!/usr/bin/env python

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_parens = ['(', '[', '{']
        right_parens = [')', ']', '}']
        stack = []
        for char in s:
            if char in left_parens:
                i = left_parens.index(char)
                stack.append(i)
            if char in right_parens:
                i = right_parens.index(char)
                if len(stack) < 1 or stack[-1] != i:
                    return False
                stack.pop()
        return len(stack) == 0



inputs = ['()', '()[]{}', '(]', '([)]', '{[]}']
expecteds = [True, True, False, False, True]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        print(f"input: {input}")
        print(f"expected: {expected}")
        actual = s.isValid(input)
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
