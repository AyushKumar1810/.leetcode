#
# @lc app=leetcode id=1856 lang=python
#
# [1856] Maximum Subarray Min-Product
#

# @lc code=start
class Solution(object):
    def maxSumMinProduct(self,nums):
        nums.append(-1)
        res = -1
        stack = []
        pre_comp_sum = [0]
        pre_comp_sum.extend(pre_comp_sum[-1] + n for n in nums)

        for index, ele in enumerate(nums):
            if stack and ele < stack[-1][1]:
                last_index = -1
                while stack and stack[-1][1] >= ele:
                    last_index, last_ele = stack.pop()
                    new_res = last_ele * (pre_comp_sum[index] - pre_comp_sum[last_index])
                    res = max(res, new_res)
                stack.append((last_index, ele))
            else:
                stack.append((index, ele))
        return res %(10**9+7)

        
# @lc code=end

