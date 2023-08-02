#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start

#NOTE : the questiom "permutations " is same as " Anagaram "question 
class Solution:
    def checkInclusion(self , s1, s2):
        def char_to_index(char):
            return ord(char) - ord('a')

        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        target_counts = [0] * 26
        window_counts = [0] * 26

        for char in s1:
            target_counts[char_to_index(char)] += 1

        for i in range(n2):
        # Add the rightmost character to the window
            window_counts[char_to_index(s2[i])] += 1

        # Remove the leftmost character from the window
            if i >= n1:
                window_counts[char_to_index(s2[i - n1])] -= 1

        # Compare the character counts in the window with the target counts
            if window_counts == target_counts:
                return True

        return False

# Example usage:
# s1 = "ab"
# s2 = "eidbaooo"
# result = checkInclusion(s1, s2)
# print(result)  # Output: True

        
# @lc code=end

