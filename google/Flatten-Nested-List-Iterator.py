#!/usr/bin/env python


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger(object):

    def __init__(self, nested):
        self.items = nested
        self.is_list = True if type(nested) == list else False

    def __str__(self):
        if self.is_list:
            return '[' + ', '.join(map(lambda item: str(item), self.items)) + ']'
        else:
            return str(self.items.getInteger())

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return not self.is_list

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.items if self.isInteger() else None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.items if not self.isInteger() else None

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flattened = []

        def flatten(sub_list):
            if sub_list.isInteger():
                self.flattened.append(sub_list.getInteger())
                return
            else:
                for item in sub_list.getList():
                    flatten(item)

        for item in nestedList:
            flatten(item)
        self.index = 0

    def next(self):
        """
        :rtype: int
        """
        next_item = self.flattened[self.index]
        self.index += 1
        return next_item


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.flattened)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

inputs = [[NestedInteger([NestedInteger(1),
                          NestedInteger(1)]),
           NestedInteger(2),
           NestedInteger([NestedInteger(1),
                          NestedInteger(1)])],

          [NestedInteger(1),
           NestedInteger([NestedInteger(4),
                          NestedInteger([NestedInteger(6)])])],

          [NestedInteger(0)]]
expecteds = [[1,1,2,1,1], [1,4,6], [0]]

if __name__ == '__main__':
    for input, expected in zip(inputs, expecteds):
        i, actual = NestedIterator(input), []
        while i.hasNext():
            actual.append(i.next())
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
