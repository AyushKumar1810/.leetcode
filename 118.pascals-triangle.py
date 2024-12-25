#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
#NOTE: We can solve this Problem by using nCr where n will Be pascal traiangle size and r will be row no we have to find 
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0: 
            return []

        pascal_triangle = [[1]]  # First row is always [1] in Pascal's Triangle 

        for i in range(1, numRows):
            prev_row = pascal_triangle[-1] # Get the previous row from the triangle 
            new_row = [1] # First element of every row is 1 in Pascal's Triangle 

            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j]) # Calculate the value of the element by adding the two elements from the previous row 

            new_row.append(1) # Last element of every row is 1 in Pascal's Triangle 
            pascal_triangle.append(new_row)
 
        return pascal_triangle



        
# @lc code=end

class Solution: 
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        pascal_triangle = [[1]]
        for i in range(1, numRows):
            prev_row = pascal_triangle[-1]
            new_row = [1]
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
            new_row.append(1)
            pascal_triangle.append(new_row)
        return pascal_triangle
