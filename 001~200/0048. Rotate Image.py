class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix[0])
        for i in range (length):
            # print(i)
            temp = [row[i] for row in matrix[:length]]
            # print(temp)
            temp.reverse()
            # print(temp)
            matrix.append(temp)
            # print(matrix)
        del matrix[:length]

            