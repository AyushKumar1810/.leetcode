#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
#NOTE:dfs each cell, keep track of visited, and track which reach pac, atl; dfs on cells adjacent to pac, atl, find overlap of cells that are visited by both pac and atl cells;

class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(row, col, reachable):
        # Mark the cell as reachable
            reachable.add((row, col))

        # Explore neighboring cells (up, down, left, right)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc

            # Check if the neighbor is a valid cell within the matrix boundaries
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in reachable:
                # Flow to the neighbor only if water can flow from higher/equal height to lower height
                    if heights[r][c] >= heights[row][col]:
                        dfs(r, c, reachable)

    # Starting from the first row and the leftmost column, perform DFS to check for cells
    # that are reachable by water from the Pacific ocean.
        for col in range(cols):
            dfs(0, col, pacific_reachable)
        for row in range(rows):
            dfs(row, 0, pacific_reachable)

    # Starting from the last row and the rightmost column, perform DFS to check for cells
    # that are reachable by water from the Atlantic ocean.
        for col in range(cols):
            dfs(rows - 1, col, atlantic_reachable)
        for row in range(rows):
            dfs(row, cols - 1, atlantic_reachable)

    # Find the cells that are reachable from both oceans
        result = list(pacific_reachable.intersection(atlantic_reachable))

        return result


# @lc code=end

