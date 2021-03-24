class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s_list =s.split()
        if len(s_list) > 0:
            return len(s_list[len(s_list)-1])
        else:
            return 0