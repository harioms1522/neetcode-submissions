from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = defaultdict(int)
        for num in nums: 
            frequencies[num] += 1

        # basically we are sorting a list of tuples
        # key on which this tuple will be sorted and 
        # order is reversed 
        sorted_freq = dict(sorted(frequencies.items(), key= lambda item: item[1], reverse=True))

        return list(sorted_freq.keys())[:k]