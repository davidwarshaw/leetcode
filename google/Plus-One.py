#!/usr/bin/env python

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        digits.append(0)
        new_digits = []
        carry = True
        for digit in digits:
            new_digit = digit

            if carry:
                new_digit += 1
                carry = False

            if new_digit > 9:
                new_digit = 0
                carry = True

            new_digits.append(new_digit)

        new_digits.reverse()
        return new_digits if new_digits[0] != 0 else new_digits[1:]


inputs = [[1,2,3], [4,3,2,1], [9, 9], [0]]
expecteds = [[1,2,4], [4,3,2,2], [1, 0, 0], [1]]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        print(f"input: {input}")
        print(f"expected: {expected}")
        actual = s.plusOne(input)
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
