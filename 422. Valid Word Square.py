# 422. Valid Word Square
# Given a sequence of words, check whether it forms a valid word square.

# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

# Note:

# The number of words given is at least 1 and does not exceed 500.
# Word length will be at least 1 and does not exceed 500.
# Each word contains only lowercase English alphabet a-z.
# Example 1:

# Input:
# [
#   "abcd",
#   "bnrt",
#   "crmy",
#   "dtye"
# ]

# Output:
# true

# Explanation:
# The first row and first column both read "abcd".
# The second row and second column both read "bnrt".
# The third row and third column both read "crmy".
# The fourth row and fourth column both read "dtye".

# Therefore, it is a valid word square.
# Example 2:

# Input:
# [
#   "abcd",
#   "bnrt",
#   "crm",
#   "dt"
# ]

# Output:
# true

# Explanation:
# The first row and first column both read "abcd".
# The second row and second column both read "bnrt".
# The third row and third column both read "crm".
# The fourth row and fourth column both read "dt".

# Therefore, it is a valid word square.
# Example 3:

# Input:
# [
#   "ball",
#   "area",
#   "read",
#   "lady"
# ]

# Output:
# false

# Explanation:
# The third row reads "read" while the third column reads "lead".

# Therefore, it is NOT a valid word square.

class Solution: 
    def validWordSquare(self,words):
        for i in range(len(words)):#iterate through the length of the words list 
            for j in range(len(words[i])):  #iterate through the length of the words[i] list 
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]: #check if the word at the current position is equal to the word at the same position in th other list 
                    return False
                return True
#example 1
words = ["abcd","bnrt","crm","dt"]
print(Solution().validWordSquare(words)) #True
#example 2
words = ["abcd","bnrt","crm","dt"]
print(Solution().validWordSquare(words)) #True