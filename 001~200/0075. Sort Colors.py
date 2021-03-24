class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        locat = 0
        for i in range (len(nums)):
            #print(nums,locat)
            if nums[locat] == 0:
                s = nums.pop(locat)
                nums.insert(0,s)
                locat+=1
                
            elif nums[locat] == 2:
                s = nums.pop(locat)
                nums.insert(len(nums),s)
            
            else:
                locat+=1
