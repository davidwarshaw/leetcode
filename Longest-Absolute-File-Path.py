#!/usr/bin/env python

import re

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        dirs = []
        max_length = 0
        prev_tab_count = -1
        tokens = input.split('\n')
        for token in tokens:
            dir = token.lstrip('\t')
            tab_count = len(token) - len(dir)
            if tab_count <= prev_tab_count:
                path = '/'.join(dirs)
                if re.search(r'\..+', path):
                    max_length = max(max_length, len(path))
            dirs = dirs[:tab_count]
            dirs.append(dir)
            prev_tab_count = tab_count
        else:
            path = '/'.join(dirs)
            if re.search(r'\..+', path):
                max_length = max(max_length, len(path))

        return max_length

inputs = ['dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext',
          'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext',
          'dir\n\tsubdir1\ndir2\n\tsubdir1',
          'a',
          '',
          'file1.ext']
expecteds = [20, 32, 0, 0, 0, 9]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.lengthLongestPath(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
