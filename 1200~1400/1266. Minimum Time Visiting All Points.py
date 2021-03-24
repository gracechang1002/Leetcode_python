class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        a = 0
        b = 0
        times = 0
        for i in range (1,len(points)):
            a = points[i-1][0]-points[i][0]
            b = points[i-1][1]-points[i][1]
            times+=max(abs(a),abs(b))
        return times