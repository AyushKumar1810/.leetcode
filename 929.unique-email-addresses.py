#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails):
        unique=set()
        for e in emails:
                i=0
                local=""
                while e[i] not in ["@" , "+"]:
                    if e[i]!=".":
                        local=local + e[i]
                    i=i+1
                while e[i]!="@":
                     i=i+1
                doamin=e[i+1:]
                unique.add((local , doamin))
        return len(unique)
        
# @lc code=end

