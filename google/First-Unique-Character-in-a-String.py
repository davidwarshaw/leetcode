#!/usr/bin/env python

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        for i, char in enumerate(s):
            chars[char] = i if char not in chars else len(s) + 1

        min_i = len(s) + 1
        for char, i in chars.items():
            min_i = min(min_i, i)
        return min_i if min_i < len(s) else -1


inputs = ['leetcode', 'loveleetcode']
expecteds = [0, 2]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.firstUniqChar(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
