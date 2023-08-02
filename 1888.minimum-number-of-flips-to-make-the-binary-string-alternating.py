#
# @lc app=leetcode id=1888 lang=python3
#
# [1888] Minimum Number of Flips to Make the Binary String Alternating
#

# @lc code=start
class Solution:
    def minFlips(self, s: str) -> int:
        
        n = len(s)
        s = s + s  # Duplicate the string to handle wrap-around cases
        target_1 = "01" * n # it will give 01010101010101
        target_2 = "10" * n # It will give 10101010101010

    # Count the number of differences between the string and target string
        def count_diff(string, target):
            return sum(s[i] != target[i] for i in range(len(string)))

    # Initialize minimum flips with the length of the original string
        min_flips = n

    # Slide the window and find the minimum flips
        for i in range(n):
            window = s[i:i+n]
            flips = min(count_diff(window, target_1), count_diff(window, target_2))
            min_flips = min(min_flips, flips)

        return min_flips

# Example usage:
# binary_string = "010010011"
# result = minFlips(binary_string)
# print(result)  # Output: 2

        
# @lc code=end

