#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}   
    # Iterate through nums2 to find the next greater element for each element
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)   
    # Find the next greater element for each element in nums1
        result = []
        for num in nums1:
            result.append(next_greater.get(num, -1)) # If the element has no next greater element, append -1 to the result  
        return result
class Solution: 
# Example usage
# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
# result = nextGreaterElement(nums1, nums2)
# print(result)  # Output: [-1, 3, -1]

        
# @lc code=end

