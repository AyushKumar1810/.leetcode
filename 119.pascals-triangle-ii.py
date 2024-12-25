#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self,rowIndex):
        if rowIndex == 0:
            return [1]

        prev_row = [1]
        for i in range(1, rowIndex + 1):
            curr_row = [1]
            for j in range(1, i):
                curr_row.append(prev_row[j - 1] + prev_row[j])
            curr_row.append(1)
            prev_row = curr_row

        return prev_row


# # Example usage:
# if __name__ == "__main__":
#     k = 3
#     row = getRow(k)
#     print("Row", k, "of Pascal's Triangle:", row)
# )


# @lc code=end

