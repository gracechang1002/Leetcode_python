class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        i = 1
        
        while i <= len(nums):
            if nums[i-1] >= target:
                return i-1
            i+=1
        return len(nums)
