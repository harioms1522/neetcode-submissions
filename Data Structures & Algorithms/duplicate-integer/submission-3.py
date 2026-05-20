class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        for num in nums: 
            if count_map.get(num, 0)>0:
                count_map[num] += 1
                return True
            else: 
                count_map[num] = 1
        return False
            