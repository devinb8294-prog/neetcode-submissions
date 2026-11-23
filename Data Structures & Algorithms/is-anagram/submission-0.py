class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}
        hash2 = {}
        for i in range(len(s)):
            if s[i] in hash1:
                hash1[s[i]] += 1
            else:
                hash1[s[i]] = 1

        for k in range(len(t)):
            if t[k] in hash2:
                hash2[t[k]] += 1
            else:
                hash2[t[k]] = 1
        
        return hash1 == hash2