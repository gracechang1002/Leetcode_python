class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        for i in range (len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]
        """
        i = 0
        while len(nums)>1:
            print(nums)
            while nums.count(nums[i])!=1:
                nums.remove(nums[i])
            i+=1
        return [i]
        
        """