class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num = len(nums)//2
        array_x = list(range(num))
        array_y = list(range(num))
        
        for i in range(num):
            array_x[i] = nums[i]
            
        for j in range(num):
            array_y[j] = nums[j+num]
        
        temp = 0
        for k in range(len(nums)):
            if k%2 == 0:
                nums[k] = array_x[temp]
            else:
                nums[k] = array_y[temp]
                temp +=1
        return nums