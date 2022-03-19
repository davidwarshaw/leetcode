#!/usr/bin/env python

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        found = False

        def prefix_redundant(prefix, larger_prefix):
            if prefix == larger_prefix:
                return False
            if len(larger_prefix) < len(prefix):
                return False
            if len(larger_prefix) % len(prefix) != 0:
                return False
            repeats = len(larger_prefix) // len(prefix)
            if prefix * repeats != larger_prefix:
                return False
            return True


        redundancies = {}
        for larger_word in wordDict:
            redundancies[larger_word] = []
            for smaller_word in wordDict:
                if prefix_redundant(smaller_word, larger_word):
                    redundancies[larger_word].append(smaller_word)

        def find(left):
            if not set(left).issubset(set(''.join(wordDict))):
                return False
            if left == '':
                return True
            prefixes = [word for word in wordDict if left.startswith(word)]
            prefixes.sort(key=lambda prefix: len(prefix), reverse=True)

            non_redundant_prefixes = prefixes.copy()
            for prefix in prefixes:
                for redundancy in redundancies[prefix]:
                    if redundancy in non_redundant_prefixes:
                        non_redundant_prefixes.remove(redundancy)

            for prefix in non_redundant_prefixes:
                if find(left[len(prefix):]):
                    return True
            else:
                return False

        return find(s)

inputs = [["leetcode", ["leet", "code"]],
          ["applepenapple", ["apple", "pen"]],
          ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
          ["catsandog", ["cats", "dog", "and", "cat", "sandog"]],
          ["acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb",
           ["abbcbda", "cbdaaa", "b", "dadaaad", "dccbbbc", "dccadd", "ccbdbc", "bbca", "bacbcdd",
            "a", "bacb", "cbc", "adc", "c", "cbdbcad", "cdbab", "db", "abbcdbd", "bcb", "bbdab",
            "aa", "bcadb", "bacbcb", "ca", "dbdabdb", "ccd", "acbb", "bdc", "acbccd", "d",
            "cccdcda", "dcbd", "cbccacd", "ac", "cca", "aaddc", "dccac", "ccdc", "bbbbcda", "ba",
            "adbcadb", "dca", "abd", "bdbb", "ddadbad", "badb", "ab", "aaaaa", "acba", "abbb"]],
           ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa",
             "aaaaaaaaaa"]],
           ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa",
             "aaaaaaaaaa", "ba"]]]
expecteds = [True, True, False, True, True, False, True]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.wordBreak(input[0], input[1])
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
