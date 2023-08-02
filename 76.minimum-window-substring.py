#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = [0] * 128

        for i in t:
            mp[ord(i)] += 1

        count = len(t)
        i = j = 0
        n = len(s)
        minLen = float('inf')
        minStart = 0

        while j < n:
            if mp[ord(s[j])] > 0:
                count -= 1

            mp[ord(s[j])] -= 1
            j += 1

            while count == 0:
                if j - i < minLen:
                    minLen = j - i
                    minStart = i

                mp[ord(s[i])] += 1
                if mp[ord(s[i])] > 0:
                    count += 1

                i += 1

        return s[minStart:minStart + minLen] if minLen != float('inf') else ""

        
        
# @lc code=end

