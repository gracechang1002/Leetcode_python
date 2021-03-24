class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        temp = 0
        maxmum = 0
        maxmum = max(nums)       
        for i in range (len(nums)):
                if i==nums.index(max(nums)):
                    continue
                elif (maxmum-1)*(nums[i]-1)>=temp:
                    temp = (maxmum-1)*(nums[i]-1)
        return temp