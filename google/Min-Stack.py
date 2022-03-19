#!/usr/bin/env python

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def __str__(self):
        return f"{str(self.stack)}"

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        new_min = min(x, self.getMin()) if len(self.stack) > 0 else x
        self.stack.append((x, new_min))

    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop()[0] if len(self.stack) > 0 else None

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0] if len(self.stack) > 0 else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1] if len(self.stack) > 0 else None

if __name__ == '__main__':
    minStack = MinStack()
    print(minStack)
    minStack.push(-2)
    print(minStack)
    minStack.push(0)
    print(minStack)
    minStack.push(-3)
    print(minStack)
    minStack.push(4)
    print(minStack)
    expected = -3
    actual = minStack.getMin()
    print(minStack)
    print(f"minStack.getMin()")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    expected = 4
    actual = minStack.pop()
    print(minStack)
    print(f"minStack.pop()")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    expected = -3
    actual = minStack.top()
    print(minStack)
    print(f"minStack.top()")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    expected = -3
    actual = minStack.getMin()
    print(minStack)
    print(f"minStack.getMin()")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    expected = -3
    actual = minStack.pop()
    print(minStack)
    print(f"minStack.pop()")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    expected = 0
    actual = minStack.pop()
    print(minStack)
    print(f"minStack.pop()")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    expected = -2
    actual = minStack.pop()
    print(minStack)
    print(f"minStack.pop()")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")

    # ["MinStack","push","push","push","getMin","pop","getMin"]
    # [[],[0],[1],[0],[],[],[]]
    minStack = MinStack()
    print(minStack)
    minStack.push(0)
    print(minStack)
    minStack.push(1)
    print(minStack)
    minStack.push(0)
    expected = 0
    actual = minStack.getMin()
    print(minStack)
    print(f"minStack.getMin()")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    expected = 0
    actual = minStack.pop()
    print(minStack)
    print(f"minStack.pop()")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
    expected = 0
    actual = minStack.getMin()
    print(minStack)
    print(f"minStack.getMin()")
    print(f"expected: {expected}")
    print(f"actual: {actual}")
    print(f"{actual == expected}")
