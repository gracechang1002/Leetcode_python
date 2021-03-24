class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        i=1
        output = 0
        
        while i <= len(arr):
            for j in range (0,len(arr)-i+1):
                output += sum(arr[j:j+i])
                #print(arr[j:j+i],sum(arr[j:j+i]),output)
            i+=2
        return output