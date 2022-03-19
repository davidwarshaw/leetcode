#!/usr/bin/env python

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.head
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        else:
            node['stop'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.head
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        else:
            if 'stop' in node:
                return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.head
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print()
    print(f"trie.insert(\"apple\")")
    expected = True
    actual = trie.search("apple")
    print()
    print(f"trie.search(\"apple\")")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    expected = False
    actual = trie.search("app")
    print()
    print(f"trie.search(\"app\")")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    expected = True
    actual = trie.startsWith("app")
    print()
    print(f"trie.startsWith(\"app\")")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    trie.insert("app");
    print()
    print(f"trie.insert(\"app\")")
    expected = True
    actual = trie.search("app")
    print()
    print(f"trie.search(\"app\")")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    trie.insert("pear");
    print()
    print(f"trie.insert(\"pear\")")
    expected = True
    actual = trie.search("pear")
    print()
    print(f"trie.search(\"pear\")")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    expected = False
    actual = trie.search("pea")
    print()
    print(f"trie.search(\"pea\")")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
