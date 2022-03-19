#!/usr/bin/env python

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = []
        next = self
        while next:
            s.append(str(next.val))
            next = next.next

        ss = " -> ".join(s)

        return f"( {ss} )"

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print("l1:")
        print(l1)
        print("l2:")
        print(l2)

        head = ListNode(0)
        current = head
        prev = None

        l1_next = l1
        l2_next = l2
        carry = 0

        while True:
            # print("sum:")
            # print(head)

            l1_digit = l1_next.val if l1_next else 0
            l2_digit = l2_next.val if l2_next else 0

            sum = l1_digit + l2_digit + carry
            digit = sum % 10

            # print(f"l1_digit: {l1_digit} l2_digit: {l2_digit} carry: {carry} -> sum: {sum}, digit: {digit}")

            if not l1_next and not l2_next and sum == 0:
                if prev:
                    prev.next = None
                break

            current.val = digit
            current.next = ListNode(0)
            prev = current
            current = current.next

            carry = 1 if sum >= 10 else 0

            l1_next = l1_next.next if l1_next else None
            l2_next = l2_next.next if l2_next else None

        # print("final sum:")
        # print(head)

        return head

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l3 = ListNode(9)
l3.next = ListNode(9)
l3.next.next = ListNode(9)
l3.next.next.next = ListNode(9)

l4 = ListNode(0)

l5 = ListNode(1)
l5.next = ListNode(0)
l5.next.next = ListNode(1)

l6 = ListNode(5)

e1 = ListNode(7)
e1.next = ListNode(0)
e1.next.next = ListNode(8)

e2 = ListNode(1)
e2.next = ListNode(4)
e2.next.next = ListNode(3)
e2.next.next.next = ListNode(0)
e2.next.next.next.next = ListNode(1)

e3 = ListNode(2)
e3.next = ListNode(0)
e3.next.next = ListNode(2)

e4 = ListNode(0)
e4.next = ListNode(1)

inputs = [[l1, l2], [l1, l3], [l2, l4], [l4, l4], [l5, l5], [l6, l6]]
expecteds = [e1, e2, l2, l4, e3, e4]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.addTwoNumbers(input[0], input[1])
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
