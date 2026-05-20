class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_maps = {} #abc: [i,j,k]
        
        for i, s in enumerate(strs):
            sorted_str = "".join(sorted(s))
            if sorted_str not in sorted_maps:
                sorted_maps[sorted_str] = [i]
            else:
                sorted_maps[sorted_str].append(i)
        response = []
        for key, indices in sorted_maps.items():
            resp_list = []
            for i in indices:
                resp_list.append(strs[i])
            response.append(resp_list)

        return response




        