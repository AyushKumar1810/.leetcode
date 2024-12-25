#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums):
        for n in nums:
            i=abs(n)-1 # 0 based index 
            nums[i]=-1*abs(nums[i]) # mark the index as negative 
        res=[]
        for i,n in enumerate(nums): # if the index is not marked as negative, then it is missing  
            if n > 0: 
                res.append(i+1) # add the missing number to the result list 
        return res
        
# @lc code=end

