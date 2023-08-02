#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start

#NOTE: basically we will use the concept of dfs and inshort we have to find all the times 1 is adjacent 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
    # Check if the grid is empty
        if not grid:
            return 0

    # Define the helper function for DFS traversal
        def dfs(row, col):
        # Base case: If the cell is out of bounds or it is water (0), return
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0': 
#NOTE:* row < 0: The row index is negative, which means it is outside the grid's top boundary.
# 1.col < 0: The column index is negative, which means it is outside the grid's left boundary.
#2. row >= len(grid): The row index is greater than or equal to the number of rows in the grid, which means it is outside the grid's bottom boundary.
#3. col >= len(grid[0]): The column index is greater than or equal to the number of columns in the grid, which means it is outside the grid's right boundary.
# 4.grid[row][col] == '0': The cell at position (row, col) contains '0', indicating that it represents water (not land).
                return

        # Mark the current cell as visited (0 represents visited or water)
            grid[row][col] = '0'

        # Explore all adjacent cells in four directions (up, down, left, right)
            dfs(row - 1, col)  # Up
            dfs(row + 1, col)  # Down
            dfs(row, col - 1)  # Left
            dfs(row, col + 1)  # Right

    # Initialize the count of islands
        num_islands = 0

    # Loop through each cell in the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
            # If the cell is land (1), start the DFS traversal from that cell
                if grid[row][col] == '1': # If at any where in matrix we arer getting 1 we will increament iland value to 1 as we have got atleast 1 island and we will do dfs here
                # Increment the number of islands as we found a new one
                    num_islands += 1
                # Start DFS traversal from the current land cell to mark its connected land cells as visited
                    dfs(row, col)

    # Return the total count of islands
        return num_islands

# Example usage:
# grid = [
#     ['1', '1', '0', '0', '0'],
#     ['1', '1', '0', '0', '0'],
#     ['0', '0', '1', '0', '0'],
#     ['0', '0', '0', '1', '1']
# ]
# result = numIslands(grid)
# print(result)  # Output: 3

# Example usage:
# grid = [
#     ['1', '1', '0', '0', '0'],
#     ['1', '1', '0', '0', '0'],
#     ['0', '0', '1', '0', '0'],
#     ['0', '0', '0', '1', '1']
# ]
# result = numIslands(grid)
# print(result)  # Output: 3

        
        
# @lc code=end

