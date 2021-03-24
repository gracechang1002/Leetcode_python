class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        temp = 0
        
        for i in range (len(accounts)):
            if sum(accounts[i]) >= temp:
                temp = sum(accounts[i])
        return temp