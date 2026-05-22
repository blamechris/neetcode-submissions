class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutiveOnes = 0
        ans = 0
        for val in nums:
            if val == 1:
                ans += 1
            else:
                maxConsecutiveOnes = max(ans, maxConsecutiveOnes)
                ans = 0
        maxConsecutiveOnes = max(ans, maxConsecutiveOnes)
        return maxConsecutiveOnes
