#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     self.dfs(sorted(nums) , 0 ,[] , res)
    #     return res
    # def dfs (self , nums , index ,path , res ):
    #     res.append (path)
    #     for i in range(index , len(nums)):
    #         self.dfs(nums , i+1 , path + [nums[i]] , res )
        result = []
    
        def backtrack(start, current_subset):
            result.append(current_subset[:])  # Add the current subset to the result
        
            for i in range(start, len(nums)):
                current_subset.append(nums[i])  # Include the current element
                backtrack(i + 1, current_subset)  # Recurse with the next index
                current_subset.pop()  # Backtrack by removing the last element
    
        backtrack(0, [])  # Start with an empty subset at index 0
        return result

# Example usage
# nums = [1, 2, 3]
# result = subsets(nums)
# print(result)  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]


# @lc code=end

