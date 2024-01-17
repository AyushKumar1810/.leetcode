#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self ,n):
        nums = list(str(n))
    
    # Find the first pair of adjacent digits in reverse order such that nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
    
    # If no such pair is found, it means the given number is the largest possible, so return -1
        if i == -1:
            return -1
    
    # Find the smallest digit to the right of nums[i] but larger than nums[i]
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
    
    # Swap nums[i] and the smallest larger digit to its right
        nums[i], nums[j] = nums[j], nums[i]
    
    # Reverse the digits to the right of nums[i] to get the smallest permutation
        nums[i + 1:] = reversed(nums[i + 1:])
    
        result = int(''.join(nums))
    
    # Return -1 if the result exceeds the 32-bit integer limit
        return result if result <= (2**31 - 1) else -1        
# @lc code=end

