#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # n= len(nums)
        # count=0
        # for i in range(n):
        #     sum=0
        #     for j in range(i,n):
        #         sum+=nums[j]
        #         if sum == k:
        #             count+=1 
        # return count
        n = len(nums) # size of the given array.
        mpp = defaultdict(int)
        preSum = 0
        cnt = 0

        mpp[0] = 1 # Setting 0 in the map.
        for i in range(n):
        # add current element to prefix Sum:
            preSum += nums[i]

        # Calculate x-k:
            remove = preSum - k

        # Add the number of subarrays to be removed:
            cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
            mpp[preSum] += 1

        return cnt
# @lc code=end

