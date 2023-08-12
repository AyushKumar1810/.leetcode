#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()  # Sort the array to handle duplicates
        result = []
    
        def backtrack(start, current_subset):
            result.append(current_subset[:])  # Add the current subset to the result
        
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # Skip duplicate elements
                current_subset.append(nums[i])  # Include the current element
                backtrack(i + 1, current_subset)  # Recurse with the next index
                current_subset.pop()  # Backtrack by removing the last element
    
        backtrack(0, [])  # Start with an empty subset at index 0
        return result

# Example usage
# nums = [1, 2, 2]
# result = subsetsWithDup(nums)
# print(result)  # Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

# @lc code=end

