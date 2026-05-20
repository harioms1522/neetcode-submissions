from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # no str sorting solution

        # important no need to assign a list if key not present
        counter_map = defaultdict(list) 
        
        # here the key will be an array[26]
        # and this key will represent strings correctly
        for s in strs:
            counter_key = [0]*26
            for c in s:
                counter_key[ord(c)-ord("a")] += 1

            counter_map[tuple(counter_key)].append(s)
        return list(counter_map.values())