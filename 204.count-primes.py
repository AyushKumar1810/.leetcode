#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        isPrime = [True] * n
        isPrime[0] = isPrime[1] =False

        for i in range(2, int(n**0.5) + 1):
            if isPrime[i] == True:
                for j in range(i*i, n, i):
                    isPrime[j] = False

        primrCount = 0
        for i in range(2, n):
            if isPrime[i] == True:
                primrCount += 1

        return primrCount
        

        
# @lc code=end

