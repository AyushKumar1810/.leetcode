#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
#NOTE:Algorithm:

# Initialize a 2D DP array dp of size (len(s) + 1) x (len(t) + 1) with all elements initialized to zero.
# Initialize the first row of dp such that dp[0][j] = 0 for all j since there is no way to form any subsequences of t in an empty string s.
# Initialize the first column of dp such that dp[i][0] = 1 for all i since there is exactly one way to form an empty subsequence of t in any non-empty string s.
# Iterate over s and t using two nested loops:
# If s[i-1] == t[j-1], then dp[i][j] = dp[i-1][j-1] + dp[i-1][j].
# If s[i-1] != t[j-1], then dp[i][j] = dp[i-1][j].
# Return dp[len(s)][len(t)], which represents the number of distinct subsequences of t in s.
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s) , len(t)
        dp = [[0]*(n+1) for _ in range(m+1)] # If only t is there and s = 0 then no possibilities 
        for i in range(m+1):
            dp[i][0]=1 #If only s are there then only 1 possibility
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else :
                    dp[i][j]=dp[i-1][j]
        return dp[m][n]
# @lc code=end

