#!/usr/bin/env python

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""

        for i in range(len(s)):
            current = ""
            for j in s[i:]:
                if j in current:
                    break
                current += j

            if len(current) > len(longest):
                longest = current

        return len(longest)

inputs = ["abcabcbb", "bbbbb", "pwwkew", "", "abcdef"]
expecteds = [3, 1, 3, 0, 6]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.lengthOfLongestSubstring(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
