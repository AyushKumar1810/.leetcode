#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def backtrack(start , current_partitions):
            if start ==len(s):
                result.append(current_partitions[:])
                return
            for end in range (start + 1 ,len(s)+1) :
                if s[start:end] == s[start:end][::-1]:
                    current_partitions.append(s[start:end])
                    backtrack(end ,current_partitions)
                    current_partitions.pop()
        backtrack(0,[])
        return result


        
# @lc code=end

