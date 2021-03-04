class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        unique = set()
        for num in A:
            if num not in unique:
                unique.add(num)
            else:
                return num