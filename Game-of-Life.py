#!/usr/bin/env python

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        h = len(board)
        w = len(board[0])
        def neighbor_count(x, y):
            total = 0
            for ny in range(max(0, y - 1), min(h, y + 2)):
                for nx in range(max(0, x - 1), min(w, x + 2)):
                    if nx != x or ny != y:
                        total += board[ny][nx] % 2
            return total

        for y in range(h):
            for x in range(w):
                nc = neighbor_count(x, y)
                val = board[y][x]
                if val % 2 == 0:
                    if nc == 3:
                        board[y][x] += 2
                if val % 2 == 1:
                    if nc < 2 or nc > 3:
                        board[y][x] += 2

        for y in range(h):
            for x in range(w):
                val = board[y][x]
                if val > 1:
                    board[y][x] = 1 if val % 2 == 0 else 0

inputs = [[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]]
expecteds = [[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        print('input:')
        for row in input:
            print(row)
        print('expected:')
        for row in expected:
            print(row)
        s.gameOfLife(input)
        actual = input
        print('actual:')
        for row in actual:
            print(row)
        print(f"{actual == expected}")
        print()
