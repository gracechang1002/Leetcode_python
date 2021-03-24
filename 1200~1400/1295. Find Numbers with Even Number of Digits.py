class Solution:
    def findNumbers(self, nums: List[int]) -> int:

#==========11111111111111111=============== 
#         times=0
        
#         for i in range (len(nums)):
#             if len(str(nums[i]))%2 == 0:
#                 times+=1
#         return times    

#==========22222222222222222=============== 
        times=0
        for i in nums:
            if len(str(i)) % 2 == 0:
                times+=1
        return times


