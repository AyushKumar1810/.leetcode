#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates , target ):
        ans = []
        ds=[]
        candidates.sort()
        def find_combinations(index,target):
            if target==0:
                ans.append(ds[:])
                return 
            for i in range(index,len(candidates)):
                if i > index and candidates[i]==candidates[i-1]: # We don't want duplicate so we will skip it if we found out
                    continue
                if candidates[i] > target: # Also we the number is greater than target then we will jump out of loop 
                    break
                ds.append(candidates[i]) # If not then just add to ds
                find_combinations(i+1,target-candidates[i]) # and do recursively for next element till remaining value 
                ds.pop()
        find_combinations(0,target)
        return ans 
                           

# @lc code=end

