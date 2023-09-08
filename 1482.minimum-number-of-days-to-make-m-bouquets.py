#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
    # Helper function to check if it's possible to make m bouquets
    # with k adjacent flowers or more given a specific day as the maximum bloom day
        def check(day):
            consecutive_blooms = 0  # Counter for consecutive bloomed flowers
            bouquets = 0  # Counter for bouquets made

            for bloom in bloomDay:
                if bloom <= day:  # If the flower can be used to make a bouquet
                    consecutive_blooms += 1
                    if consecutive_blooms == k:  # If enough consecutive flowers are available
                        bouquets += 1
                        consecutive_blooms = 0  # Reset the counter
                else:
                    consecutive_blooms = 0  # Reset the counter if a flower can't be used

            return bouquets >= m  # Return True if enough bouquets can be made

    # If the total number of flowers is less than m * k, it's impossible to make m bouquets
        if len(bloomDay) < m * k:
            return -1

        left = min(bloomDay)  # Minimum possible day (earliest bloom)
        right = max(bloomDay)  # Maximum possible day (latest bloom)

        while left < right:
            mid = left + (right - left) // 2  # Calculate the middle day

            if check(mid):
                right = mid  # If it's possible to make m bouquets with mid as max bloom day, update the right boundary
            else:
                left = mid + 1  # If not possible, update the left boundary

        return left  # Return the minimum number of days required to make m bouquets

# Example usage:
# bloomDay = [1, 10, 3, 10, 2]
# m = 3
# k = 1
# result = minDays(bloomDay, m, k)
# print(result)  # Output: 3

# @lc code=end

