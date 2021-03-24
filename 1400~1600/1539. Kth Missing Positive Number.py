class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        i = 0
        temp = 0
        
        while temp < k:
            i+=1
            if i not in arr:
                temp+=1
        return i
    
            