#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                # Count the perimeter for each land cell

                # Check the top cell
                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 1

                # Check the bottom cell
                    if i == rows - 1 or grid[i + 1][j] == 0:
                        perimeter += 1

                # Check the left cell
                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 1

                # Check the right cell
                    if j == cols - 1 or grid[i][j + 1] == 0:
                        perimeter += 1

        return perimeter

        
# @lc code=end

