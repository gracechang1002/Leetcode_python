class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        bin_bit = [str(bin(i)[2:]).count('1') for i in sorted(arr)]
        # print(bin_bit)
        bin_bit = sorted(range(len(bin_bit)), key=lambda k: bin_bit[k])
        # print(bin_bit)
        bin_bit = [sorted(arr)[i] for i in bin_bit]
        # print(output)
        
        return bin_bit
        