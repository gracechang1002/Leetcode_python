class Solution:
    def maximum69Number (self, num: int) -> int:
        
        num_list = [int(i) for i in str(num)]
        num_new = num
        
        for i in range (len(num_list)):
            num_list = [int(i) for i in str(num)]
            if num_list[i]==6:
                num_list[i]=9
                if int(''.join(str(j) for j in num_list)) > num_new:
                    num_new = int(''.join(str(j) for j in num_list))
        return num_new
            