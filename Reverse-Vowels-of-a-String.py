#!/usr/bin/env python

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_lookup = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        vowels = []
        reversed = ''
        for char in s:
            if char in vowel_lookup:
                vowels.append(char)
        for char in s:
            if char in vowel_lookup:
                reversed += vowels.pop()
            else:
                reversed += char
        return reversed

inputs = ['hello', 'leetcode', 'aA']
expecteds = ['holle', 'leotcede', 'Aa']

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.reverseVowels(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
