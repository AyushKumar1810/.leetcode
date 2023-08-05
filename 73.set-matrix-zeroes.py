#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
#NOTE:we are making a two hash map row , col , if we found 0 then we will mark that row and col hashmap value to 1 and we will contunue and after that we will re itterate and go to it and when we wfind 1 in col or 1 in row hashmap we will make it all col or row to 0 ..

#NOTE:The steps are as follows:

# First, we will declare two arrays: a row array of size N and a col array of size M and both are initialized with 0.
# Then, we will use two loops(nested loops) to traverse all the cells of the matrix.
# If any cell (i,j) contains the value 0, we will mark ith index of row array i.e. row[i] and jth index of col array col[j] as 1. It signifies that all the elements in the ith row and jth column will be 0 in the final matrix.
# We will perform step 3 for every cell containing 0.
# Finally, we will again traverse the entire matrix and we will put 0 into all the cells (i, j) for which either row[i] or col[j] is marked as 1.
# Thus we will get our final matrix.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0]) # we are making new row and col
        Rows=[0]*rows# initializing it to 0
        Cols=[0]*cols # Initializing it to 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0: # If we found 0 
                    Rows[i]=1 #we will change our rows and cols value of that index to 1 
                    Cols[j]=1 # same things happens to coloumn
        for i in range(rows):
            for j in range(cols):
                if Rows[i] or Cols[j]: # we are retraversing if we are getting 1 then that means we have to make that respective coloumn or row to 0 
                    matrix[i][j]=0
        return matrix


# @lc code=end

