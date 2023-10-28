#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing whitespace
        if not s:
            return 0

    # Define variables for sign and result
        sign = 1
        result = 0

    # Check for the sign character
        if s[0] in ['+', '-']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

    # Iterate through the string and convert to an integer
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)

        # Check for overflow
            if sign == 1 and result > 2**31 - 1:
                return 2**31 - 1
            if sign == -1 and result > 2**31:
                return -2**31

        return sign * result

        
# @lc code=end

