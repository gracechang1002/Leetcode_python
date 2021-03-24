class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

#######第一種########

        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total
        return nums

########第二種########

        for i in range(len(nums),0,-1):
            nums[i-1] = sum(nums[:i])
        return nums
        