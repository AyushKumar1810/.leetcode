#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []  # List to store the final combinations
    
        def backtrack(start, current_combination, remaining):
        # Base case: If remaining sum is 0, add the current combination to result
            if remaining == 0:
                result.append(current_combination[:])
                return
        
        # Iterate through candidates starting from the current index
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue  # Skip candidates larger than remaining sum
            
            # Include the current candidate in the current combination
                current_combination.append(candidates[i])
            # Recurse with the same index (allowing reuse of current candidate)
                backtrack(i, current_combination, remaining - candidates[i])
            # Backtrack by removing the last candidate
                current_combination.pop()
    
    # Sort the candidates to handle duplicate combinations
        candidates.sort()
    # Start the backtracking process with an empty combination and target sum
        backtrack(0, [], target)
        return result

# Example usage
# candidates = [2, 3, 6, 7]
# target = 7
# result = combinationSum(candidates, target)
# print(result)  # Output: [[2, 2, 3], [7]]

# @lc code=end

