#!/usr/bin/env python

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def i_from_xy(x, y):
            return (y * w) + x

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        h = len(grid)
        w = len(grid[0])
        vs = [None] * h * w
        i = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == '1':
                    edges = []
                    edges.append(i_from_xy(x, y))
                    if x - 1 >= 0 and grid[y][x - 1] == '1':
                        edges.append(i_from_xy(x - 1, y))
                    if x + 1 < w and grid[y][x + 1] == '1':
                        edges.append(i_from_xy(x + 1, y))
                    if y - 1 >= 0 and grid[y - 1][x] == '1':
                        edges.append(i_from_xy(x, y - 1))
                    if y + 1 < h and grid[y + 1][x] == '1':
                        edges.append(i_from_xy(x, y + 1))
                    vs[i_from_xy(x, y)] = edges
                    i += 1

        marked = [None] * h * w
        ids = [None] * h * w
        count = 0

        def bfs(v):
            marked[v] = True
            ids[v] = count
            for w in vs[v]:
                if not marked[w]:
                    bfs(w)

        for s in range(len(vs)):
            if vs[s] and not marked[s]:
                bfs(s)
                count += 1

        clean_ids = list(filter(lambda v: v is not None, ids))
        return max(clean_ids) + 1 if len(clean_ids) > 0 else 0



inputs = [[['1', '1', '1', '1', '0'],
           ['1', '1', '0', '1', '0'],
           ['1', '1', '0', '0', '0'],
           ['0', '0', '0', '0', '0']],
          [['1', '1', '0', '0', '0'],
           ['1', '1', '0', '0', '0'],
           ['0', '0', '1', '0', '0'],
           ['0', '0', '0', '1', '1']],
          [['0']],
          [['1', '1', '1'],
           ['0', '1', '0'],
           ['1', '1', '1']]]
expecteds = [1, 3, 0, 1]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.numIslands(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
