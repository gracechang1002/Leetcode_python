class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        for i in range (len(t)):
            if t[i] in s:
                s = s.replace(t[i],"",1)
        return len(s)
    