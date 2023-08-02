#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <=r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return -1
        
# @lc code=end

