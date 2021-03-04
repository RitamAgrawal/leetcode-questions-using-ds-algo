class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            row.reverse()
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] = 0  
                else:
                    row[i] = 1
        return A
        