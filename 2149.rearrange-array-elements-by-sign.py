#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
#basically we will create 0th index for 1st ostive value and 1t index for 1st begative value as the series will be altertnate  so for next postive we will increament postive will 2 and fo negative also by 2 
        n=len(nums)
        ans=[0]*n
        postive_num , negative_num=0,1
        for i in range(n):
            if nums[i] > 0 :
                ans[postive_num] = nums[i]
                postive_num+=2
            else :
                ans[negative_num] = nums[i]
                negative_num +=2
        return ans
# @lc code=end

