#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
        result = 0
        prev_value = 0
    
        for c in s:
            value = roman_to_int[c]
            if value > prev_value:
                result += value - 2 * prev_value
            else:
                result += value
            prev_value = value
    
        return result

# Example usage
# roman_numeral = "MCMXCIV"
# integer_value = romanToInt(roman_numeral)
# print(integer_value)  # Output: 1994

        
# @lc code=end

