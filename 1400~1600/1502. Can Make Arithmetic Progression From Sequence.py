class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        i = 0
        
        while i <= (len(arr)-3):
            print(i)
            if arr[i+1]-arr[i] != arr[i+2]-arr[i+1]:
                return False
            i+=1 
        return True