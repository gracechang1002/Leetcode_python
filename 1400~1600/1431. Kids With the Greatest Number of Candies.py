class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        output=[]
        maxmum = candies.index(max(candies))
        
        for i in range(len(candies)):
            if candies[i]+extraCandies>=candies[maxmum]:
                output.append(True)
            else:
                output.append(False)
        return output



