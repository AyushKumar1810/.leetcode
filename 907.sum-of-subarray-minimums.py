#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []  # Monotonic stack to store indices
        result = 0  # Variable to store the sum of minimum elements
        MOD = 10**9 + 7

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
            # Pop elements from the stack while the current element is smaller
                popped_index = stack.pop()
                prev_index = stack[-1] if stack else -1

            # Calculate the contribution of the popped element to the result
                result += arr[popped_index] * (i - popped_index) * (popped_index - prev_index)

            stack.append(i)

    # Process remaining elements in the stack
        while stack:
            popped_index = stack.pop()
            prev_index = stack[-1] if stack else -1
            result += arr[popped_index] * (len(arr) - popped_index) * (popped_index - prev_index)

        return result % MOD

# # Example usage:
# A = [3, 1, 2, 4]
# result = sumSubarrayMins(A)
# print(result)  # Output: 17

        
# @lc code=end

