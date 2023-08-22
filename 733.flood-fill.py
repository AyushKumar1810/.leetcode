#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        # Get the original color at the starting pixel
        originalColor = image[sr][sc]
        
        # Check if the starting pixel is the same as the new color
        if originalColor == newColor:
            return image
        
        # Perform depth-first search to fill the area
        def dfs(row, col):
            # Check if the current cell is within bounds and has the original color
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != originalColor:
                return
            
            # Update the current cell's color to the new color
            image[row][col] = newColor
            
            # Recursively call dfs for neighboring cells
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        # Start the DFS from the given starting pixel
        dfs(sr, sc)
        
        return image

# Example usage
# solution = Solution()
# image = [
#     [1, 1, 1],
#     [1, 1, 0],
#     [1, 0, 1]
# ]
# sr = 1
# sc = 1
# newColor = 2
# result = solution.floodFill(image, sr, sc, newColor)
# for row in result:
#     print(row)
        
# @lc code=end

