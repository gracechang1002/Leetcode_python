class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        starts = 0
        altitudes = 0
        
        for i in range(len(gain)):
            starts += gain[i]
            if starts > altitudes:
                altitudes = starts
        return altitudes
            