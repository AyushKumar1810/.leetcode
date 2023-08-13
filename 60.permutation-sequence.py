#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        k -= 1  # Adjust k to 0-based index
    
        factorial = 1
        for i in range(2, n):
            factorial *= i
    
        permutation = []
        for i in range(n - 1, 0, -1):
            index = k // factorial
            k %= factorial
            permutation.append(numbers.pop(index))
            factorial //= i
    
        permutation.append(numbers[0])
        return ''.join(map(str, permutation))


        
# @lc code=end

