#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        start = nums[0] # start of the range 
        for i in range(len(nums)): 
            if i == len(nums) - 1 or nums[i + 1] > nums[i ] + 1:# if the next number is not in the range , then append the range to the result 
                if start == nums[i]:
                    res.append(str(start)) # if the range is only one number , append it as a string 
                else:
                    res.append(str(start) + "->" + str(nums[i])) # if the range is more than one number , append it as a string with "->" in between 
                if i != len(nums) - 1:
                    start = nums[i + 1]
        return res

        
# @lc code=end

