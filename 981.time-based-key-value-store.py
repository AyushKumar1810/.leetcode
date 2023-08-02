#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
         self.mp = {} # using hash map we are solving
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.mp:
            it = self.mp[key]
            high = len(it) - 1
            low = 0
            ans = ""

            while low <= high:
                mid = low + (high - low) // 2
                if it[mid][1] <= timestamp:
                    ans = it[mid][0]
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

