class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        l = len(mat)
        j = len(mat)-1
        for i in range(l):
            result += mat[i][i]
            if i != j-i:
                result+= mat[j-i][i]
        return result
        