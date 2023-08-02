#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []

        sequences = {}  # Hashmap to store sequences and their counts
        result = []

        for i in range(n - 9):
            sequence = s[i:i + 10]

        # Update the hashmap with the current sequence
            sequences[sequence] = sequences.get(sequence, 0) + 1

        # If the count reaches 2, add the sequence to the result
            if sequences[sequence] == 2:
                result.append(sequence)

        return result

# Example usage:
# dna_sequence = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# result = findRepeatedDnaSequences(dna_sequence)
# print(result)  # Output: ['AAAAACCCCC', 'CCCCCAAAAA']

        
# @lc code=end

