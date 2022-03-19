#!/usr/bin/env python

class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        mappings = []
        for e in A:
            mappings.append(B.index(e))
        return mappings


input =[[12, 28, 46, 32, 50],
        [50, 12, 32, 46, 28]]
expected = [1, 4, 3, 2, 0]

if __name__ == '__main__':
    s = Solution()
    actual = s.anagramMappings(input[0], input[1])
    print(f"input: {input}")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    print()
