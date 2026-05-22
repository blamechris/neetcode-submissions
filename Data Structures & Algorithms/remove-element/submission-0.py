class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr1 = 0
        ptr2 = len(nums)
        while ptr1 < ptr2:
            if nums[ptr1] == val:
                ptr2 -= 1
                nums[ptr1] = nums[ptr2]
            else:
                ptr1 += 1
        return ptr2