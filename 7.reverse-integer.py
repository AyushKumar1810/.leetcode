#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1  # Remember if the number is positive or negative
        x = abs(x)  # Make the number positive
        
        reversed_num = 0
        while x > 0:
            last_digit = x % 10  # Get the last digit of the number
            reversed_num = reversed_num * 10 + last_digit  # Add the last digit to 
            #the reversed number
            x = x // 10  # Remove the last digit from the number
        
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:# for our base condition
            return 0
        
        return reversed_num * sign


        
# @lc code=end

