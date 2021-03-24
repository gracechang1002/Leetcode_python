class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        dic = {"type":0, "color":1, "name":2}
        j=0
        for i in range(len(items)):
            # print(items[i],items[i][dic[ruleKey]],ruleValue)
            if items[i][dic[ruleKey]] == ruleValue:
                j+=1
        return j
