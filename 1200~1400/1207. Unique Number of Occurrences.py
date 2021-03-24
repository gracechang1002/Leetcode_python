class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        test = []
        arr_set = list(set(arr))
        for i in range (len(arr_set)):
            if arr.count(arr_set[i]) in test:
                 return False
            else:
                test.append(arr.count(arr_set[i]))
        return True
