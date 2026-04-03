class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                letter = ord(c) - ord('a')
                freq[letter] += 1
        
            anagram[tuple(freq)].append(s)

        return list(anagram.values())
        