#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
#NOTE : solution is quite simple we just have to trace all the array and we have to give rank to each one 1 to n , for that we will use the Hashmap that will be best for doing it so , it will give O(1) solution . 
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Step 1: Create a copy of the scores array and sort it in descending order
        sorted_scores = sorted(score, reverse=True)
        
        # Step 2: Create a dictionary to map scores to ranks
        rank_map = {}
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)
        
        # Step 3: Assign ranks to each athlete based on their scores
        answer = [rank_map[score[i]] for i in range(len(score))]
        
        return answer
        
# @lc code=end

