#!/usr/bin/env python

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        cleansed = set()
        for email in emails:
            address, at, domain = email.partition('@')
            cleansed_address = address.replace('.', '').split('+')[0]
            cleansed.add(cleansed_address + at + domain)
        return len(cleansed)


inputs = [["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]]
expecteds = [2]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.numUniqueEmails(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
