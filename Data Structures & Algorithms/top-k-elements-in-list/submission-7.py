class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        ans = []
        for num in nums:
            if num not in counts:
                counts[num] = 1 # init the value in the dict
            else:
                counts[num] += 1 # increment value as it already exists
        
        
        ans = sorted(counts, key=counts.get, reverse=True)[:k]
        return ans