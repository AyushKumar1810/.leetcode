#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
# from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        threshold = n // 3
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        result = []
        for num, count in counter.items():
            if count > threshold:
                result.append(num)

        return result

        
# @lc code=end

