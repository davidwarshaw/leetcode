#!/usr/bin/env python

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            current = ""
            # print(f"\ni: {i}")
            o_offset = -i if i > 0 else None
            r_offset = i if i > 0 else None
            for o, r in zip(s[:o_offset], list(reversed(s))[r_offset:]):
                # print(f"{o}, {r}")
                if o != r and len(current) > 0:
                    break
                elif o == r:
                    current += o
            if len(current) > len(longest):
                longest = current

        return longest

 0   abb
-1 bba

 abb
bba

abb
bba

abb
 bba

abb
  bba

inputs = ["abc", "babad", "cbbd", "radar", "aaa", "aab", "a", "abb"]
expecteds = ["b", "aba", "bb", "radar", "aaa", "aa", "a", "bb"]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.longestPalindrome(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
