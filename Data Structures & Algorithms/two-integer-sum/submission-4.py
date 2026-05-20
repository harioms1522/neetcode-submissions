class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, current in enumerate(nums):
            diff = target - current
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[current] = i

        return [-1,-1]
            