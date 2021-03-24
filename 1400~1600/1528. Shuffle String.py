class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        target = [0]*len(indices)
        lis = [chr for chr in s]
        
        for i in range (len(indices)):
            target[indices[i]] = lis[i]

        s = ''.join(str(i) for i in target)
        
        return s