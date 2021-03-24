class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        length = len(arr)
        for i in range (1,length):
            arr[i-1] = max(arr[i:length])
        arr[length-1] = -1
        return arr