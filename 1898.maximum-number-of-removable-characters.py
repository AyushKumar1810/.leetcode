#
# @lc app=leetcode id=1898 lang=python3
#
# [1898] Maximum Number of Removable Characters
#

# @lc code=start
class Solution:
    def maximumRemovals(self, s: str, p: str, removable):
        # Helper function to check if str2 is a subsequence of str1
        def is_subsequence(str1, str2, remove_set):
            i, j = 0, 0
            while i < len(str1) and j < len(str2):
                if i not in remove_set and str1[i] == str2[j]:
                    j += 1
                i += 1
            return len(str2) == j
        
        # Binary search on the removable array
        def binary_search(left, right):
            if left > right:
                return left
            
            mid = (left + right) // 2
            remove_set = set(removable[:mid + 1])
            
            if is_subsequence(s, p, remove_set):
                # If str2 is a subsequence of str1, search in the right half
                return binary_search(mid + 1, right)
            else:
                # If str2 is not a subsequence of str1, search in the left half
                return binary_search(left, mid - 1)
        
        # Call the binary search function with initial left and right pointers
        return binary_search(0, len(removable) - 1)

        
# @lc code=end

