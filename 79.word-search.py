#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start

#NOTE:question is same as the pacific ocean question ...
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
    
        def dfs(row, col, index):
        # Base case: If all letters in the word are found, return True
            if index == len(word):
                return True
        
        # Check if the current position is out of bounds or the letter does not match
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
                return False
        
        # Mark the current letter as visited
            temp = board[row][col] # we are storing value to a temeprorey variable
            board[row][col] = '#' #After that we are just putting "#" in place of original word so that we can't get the word twice,, for eg if we have word AYUSH we we have traverse "A" and we are at "Y" so will be replace "A" wuth "#" as so that we can't get to that word again
        
        # Explore neighboring cells in all directions
            found = dfs(row + 1, col, index + 1) or dfs(row - 1, col, index + 1) \
                or dfs(row, col + 1, index + 1) or dfs(row, col - 1, index + 1)
        
        # Restore the original letter after backtracking
            board[row][col] = temp
            return found

    # Start DFS from each cell in the board to search for the word
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
    
    # Word not found on the board
        return False

        
# @lc code=end

