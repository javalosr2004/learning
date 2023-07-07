class Solution:

    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        # DNA dict
        dna_dict = {}
        repeated = []
        # extract every 10 characters
        for char in range(len(s) - 9):
            current = s[char: char + 10]
            if (dna_dict.get(current)):
                dna_dict[current] += 1
            else:
                dna_dict[current] = 1
        # iterate through dictionary, if greater than one append to list
        for (key, val) in dna_dict.items():
            if val > 1:
                repeated.append(key)
        return repeated
    

s1 = Solution()

repeats = s1.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print(repeats)