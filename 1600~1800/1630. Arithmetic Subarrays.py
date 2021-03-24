class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        output = []
        
        for i in range (len(l)):
            temp = sorted(nums[l[i]:r[i]+1])
            j = 0
            while j < len(temp)-2:
                if temp[j+1] - temp[j] != temp[j+2] - temp[j+1]:
                    output.append(False)
                    break
                j+=1
            else:
                output.append(True)
            # print(output)
        return output