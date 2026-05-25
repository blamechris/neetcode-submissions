class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = {}
        ans = []
        for i, val in enumerate(nums):
            if val not in solutions:
                solutions[target - val] = i
            else:
                ans = [solutions[val], i]
                
        return ans

                