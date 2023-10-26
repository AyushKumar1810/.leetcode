#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
#NOTE:First, we check if the input array strs is empty. If it is, we return an empty string because there is no common prefix to find.

# We sort the array strs so that the first string in the sorted array is the shortest, and the last string is the longest.

# We initialize an empty string prefix to store the common prefix.

# We iterate through the characters of the shortest string (strs[0]) and compare them with the characters of the longest string (strs[-1]). If the characters match, we add them to the prefix. If there is a mismatch, we break the loop.

# Finally, we return the prefix, which is the longest common prefix among the strings.

# Example:
# Suppose we have the input strs = ["flower", "flour", "flourish"]. The common prefix is "flo." The function would return "flo" for this input.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
    #     if not strs:
    #         return ""

    # # Find the shortest string in the array
    #     shortest = min(strs, key=len)

    #     for i, char in enumerate(shortest):
    #         for string in strs:
    #             if string[i] != char:
    #                 return shortest[:i]

    #     return shortest
            
        if not strs:
            return ""
    
    # Sort the array to compare the shortest and longest strings
        strs.sort()
    
    # Find the common prefix between the shortest and longest strings
        prefix = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:# strs[0][i] means 1st string and i means ith index of that string , strs[-1][i] last string with ith index value
                prefix += strs[0][i] # If the value is equal then we will put it into prefix(result) 
            else:# Otherwise break from there and will resturn the result
                break
    
        return prefix

        
# @lc code=end

