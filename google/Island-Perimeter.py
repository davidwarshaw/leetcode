#!/usr/bin/env python

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        perimeter = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == 1:
                    neighbor_count = 0
                    neighbor_count += 1 if col - 1 >= 0 and grid[row][col - 1] == 1 else 0
                    neighbor_count += 1 if col + 1 < width and grid[row][col + 1] == 1 else 0
                    neighbor_count += 1 if row - 1 >= 0 and grid[row - 1][col] == 1 else 0
                    neighbor_count += 1 if row + 1 < height and grid[row + 1][col] == 1 else 0
                    perimeter += 4 - neighbor_count
                    print(neighbor_count)
        return perimeter

inputs = [[[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]]
expecteds = [16]

if __name__ == '__main__':
    s = Solution()
    for input, expected in zip(inputs, expecteds):
        actual = s.islandPerimeter(input)
        print(f"input: {input}")
        print(f"expected: {expected}")
        print(f"actual: {actual}")
        print(f"{actual == expected}")
        print()
