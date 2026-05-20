from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted_maps = {} #abc: [str1,str3,str5]

        # very important default dict gives a default value for each key
        sorted_maps = defaultdict(list)
        
        for i, s in enumerate(strs):
            sorted_str = "".join(sorted(s))
            # now I can be sure that for ever sorted_str I can directly
            # append
            sorted_maps[sorted_str].append(strs[i])

        return list(sorted_maps.values())




        