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

        pascal_triangle = [[1]]  # First row is always [1]

        for i in range(1, numRows):
            prev_row = pascal_triangle[-1]
            new_row = [1]

            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])

            new_row.append(1)
            pascal_triangle.append(new_row)

        return pascal_triangle
    # def calculateBinomialCoefficient(self,n, k):
    # # Calculate the factorial of a number
    #     def factorial(num):
    #         if num <= 1:
    #             return 1
    #         else:
    #             return num * factorial(num - 1)

    #     return factorial(n) // (factorial(k) * factorial(n - k))

    # def generatePascalTriangle(self,numRows):
    #     pascal_triangle = []

    #     for row in range(numRows):
    #         new_row = [calculateBinomialCoefficient(row, col) for col in range(row + 1)]
    #         pascal_triangle.append(new_row)

    #     return pascal_triangle
# Example usage:
# if __name__ == "__main__":
#     n = 5
#     pascal_triangle = generatePascalTriangle(n)
#     print("Pascal's Triangle:")
#     for row in pascal_triangle:
#         print(row)


        
# @lc code=end

