class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        numm = 0
        
        for i in range (len(arr)):
            if(arr[i]%2==1):
                numm+=1
                if numm >= 3:
                    return True
            else:
                numm=0