#
# @lc app=leetcode id=2373 lang=python3
#
# [2373] Largest Local Values in a Matrix
#

# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = []

        # Iterate through each cell except for the border cells
        for i in range(1, n - 1):
            temp_row = []
            for j in range(1, n - 1):
                temp = 0
                
                # Consider the 3x3 neighborhood centered around the current cell
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        temp = max(temp, grid[k][l])
                
                # Append the largest value in the neighborhood to the temp_row
                temp_row.append(temp)
            
            # Append the temp_row to the result
            result.append(temp_row)

        return result

        
        
# @lc code=end

