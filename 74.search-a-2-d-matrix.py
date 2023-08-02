#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # Get the number of rows and columns in the matrix
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Initialize the left and right pointers for binary search
        l, r = 0, rows*cols - 1
        
        # Perform binary search until the left pointer becomes greater than the right pointer
        while l <= r:
            # Calculate the middle index
            m = l + (r - l) // 2
            # Convert the middle index to corresponding row and column indices
            x = m // cols
            y = m % cols
            
            # Check if the element at the middle index is equal to the target
            if matrix[x][y] == target:
                # If true, the target element is found in the matrix, so return True
                return True
            elif matrix[x][y] < target:
                # If the element at the middle index is smaller than the target,
                # update the left pointer to search in the right half of the remaining elements
                l = m + 1
            else:
                # If the element at the middle index is greater than the target,
                # update the right pointer to search in the left half of the remaining elements
                r = m - 1
        
        # If the target element is not found in the matrix, return False
        return False


        
# @lc code=end

