#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()  # Keep track of visited numbers        
        while n != 1:
            if n in visited:  # If we have already visited this number, it's in a
                # loop
                return False
            visited.add(n)  # Add the current number to visited set            
            sum_of_squares = 0
            while n > 0:
                digit = n % 10  # Get the rightmost digit
                sum_of_squares += digit * digit  # Add the square of the digit 
                # to the sum
                n //= 10  # Remove the rightmost digit            
            n = sum_of_squares  # Update n to be the sum of squares for the next
            # iteration        
        return True  # If we reach 1, the number is happy

        
# @lc code=end

