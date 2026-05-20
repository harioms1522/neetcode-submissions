class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        counts = {}

        for c in s:
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] += 1
        
        print(counts)

        for c in t:
            if counts.get(c,0)>0:
                counts[c] -= 1
        
        print(counts)
        for key, val in counts.items():
            if val > 0:
                return False

        return True