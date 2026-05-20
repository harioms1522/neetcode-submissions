class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {} #  diff: index
        for i, current in enumerate(nums):
            current = nums[i]
            diff = target - current
            if current in diff_map:
                return [diff_map[current], i]
            
            diff_map[diff] = i

            