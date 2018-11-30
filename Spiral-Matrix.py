#!/usr/bin/env python

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        h = len(matrix)
        w = len(matrix[0])
        #print(f"h: {h} w: {w}")

        unwound = []
        row_l = 0
        row_h = h - 1
        col_l = 0
        col_h = w - 1
        while True:

            #print(f"1: row_l: {row_l} row_h: {row_h} col_l: {col_l} col_h: {col_h}")
            if col_l == col_h + 1:
                break
            for x in range(col_l, col_h + 1):
                #print(matrix[row_l][x])
                unwound.append(matrix[row_l][x])
            row_l += 1
            #print(f"1: row_l: {row_l} row_h: {row_h} col_l: {col_l} col_h: {col_h}")

            #print(f"2: row_l: {row_l} row_h: {row_h} col_l: {col_l} col_h: {col_h}")
            if row_l == row_h + 1:
                break
            for y in range(row_l, row_h + 1):
                #print(matrix[y][col_h])
                unwound.append(matrix[y][col_h])
            col_h -= 1
            #print(f"2: row_l: {row_l} row_h: {row_h} col_l: {col_l} col_h: {col_h}")

            #print(f"3: row_l: {row_l} row_h: {row_h} col_l: {col_l} col_h: {col_h}")
            if col_l - 1 == col_h:
                break
            for x in range(col_h, col_l - 1, -1):
                #print(matrix[row_h][x])
                unwound.append(matrix[row_h][x])
            row_h -= 1
            #print(f"3: row_l: {row_l} row_h: {row_h} col_l: {col_l} col_h: {col_h}")

            #print(f"4: row_l: {row_l} row_h: {row_h} col_l: {col_l} col_h: {col_h}")
            if row_l - 1 == row_h:
                break
            for y in range(row_h, row_l - 1, -1):
                #print(matrix[y][col_l])
                unwound.append(matrix[y][col_l])
            col_l += 1
            #print(f"4: row_l: {row_l} row_h: {row_h} col_l: {col_l} col_h: {col_h}")

        return unwound

inputs = [[[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]],
          [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]],
          [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
          [[1], [2], [3], [4]],
          [[1]],
          [[1, 2], [3, 4]],
          [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]]
expecteds = [[1, 2, 3, 6, 9, 8, 7, 4, 5],
             [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             [1, 2, 3, 4],
             [1],
             [1, 2, 4, 3],
             [2, 3, 4, 7, 10, 13, 16, 15, 14, 11, 8, 5 , 6, 9, 12]]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.spiralOrder(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
