class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        arr1.sort()
        change = 0
        
        for i in range (len(arr2)):
            for j in range (len(arr1)):
                if arr2[len(arr2)-1-i] == arr1[j]:
                    change = arr1.pop(j)
                    arr1.insert(0,change)
        return arr1