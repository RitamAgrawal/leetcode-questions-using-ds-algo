class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = []
        x = 1
        for i in range(n // 2):
            output.append(x)
            output.append(-x)
            x += 1
        if n % 2 == 1:
            output.append(0)
        return output
            