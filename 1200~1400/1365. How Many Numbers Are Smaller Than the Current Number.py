class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        small = 0
        output = list(range(len(nums)))
    
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    small+=1
            output[i] = small
            small = 0
        
        return output