#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

    # Remove remaining digits from the end if needed
        stack = stack[:-k] if k > 0 else stack

    # Convert the stack to a string and remove leading zeros
        result = ''.join(stack).lstrip('0')

    # Return '0' if the result is empty, otherwise return the result
        return result if result else '0'

# Example Usage:
# num = "1432219"
# k = 3
# result = removeKdigits(num, k)
# print(result)  # Output: "1219"

        
# @lc code=end

