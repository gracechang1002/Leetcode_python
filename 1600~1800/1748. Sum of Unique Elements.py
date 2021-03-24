class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        temp = Counter(nums)
        temp_key = list(temp.keys())
        output = 0
        
        for i in range (len(temp)):
            if temp[temp_key[i]] == 1:
                output += temp_key[i]
        return output