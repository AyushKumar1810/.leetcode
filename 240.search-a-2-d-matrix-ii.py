#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#We will start from 0th row and last coloumn and after that if element is lesser than target then we will increase row by 1 and we will go down and if it's greater than target then we will decrease coloumn
        n=len(matrix)
        m=len(matrix[0])
        row = 0 
        col = m-1
        while row < n and col >=0:
            if matrix[row][col] ==target:
                return True
            elif matrix[row][col] < target:
                row = row + 1
            else :
                col=col-1
        return False


# @lc code=end

