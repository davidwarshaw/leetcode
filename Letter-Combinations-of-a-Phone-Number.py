#!/usr/bin/env python

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        combos = []
        def permute(i, prefix):
            if i == len(digits):
                return prefix
            for letter in num_to_letters[digits[i]]:
                permutation = permute(i + 1, prefix + letter)
                if permutation:
                    combos.append(permutation)

        permute(0, '')

        return combos


inputs = ["23", "678"]
expecteds = [["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
             ['mpt', 'mpu', 'mpv', 'mqt', 'mqu', 'mqv', 'mrt', 'mru', 'mrv', 'mst', 'msu', 'msv',
              'npt', 'npu', 'npv', 'nqt', 'nqu', 'nqv', 'nrt', 'nru', 'nrv', 'nst', 'nsu', 'nsv',
              'opt', 'opu', 'opv', 'oqt', 'oqu', 'oqv', 'ort', 'oru', 'orv', 'ost', 'osu', 'osv']

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.letterCombinations(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
