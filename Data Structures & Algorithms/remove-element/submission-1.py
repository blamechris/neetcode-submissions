class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leftptr = 0
        rightptr = len(nums) - 1
        ans = 0
        while leftptr <= rightptr:
            if nums[rightptr] == val:
                rightptr -= 1
            elif nums[leftptr] == val:
                nums[leftptr] = nums[rightptr]
                nums[rightptr] = val
                leftptr += 1
                ans += 1
            else:
                ans += 1
                leftptr += 1
                
        return ans
