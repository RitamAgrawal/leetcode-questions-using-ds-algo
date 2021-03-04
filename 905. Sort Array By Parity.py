class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        while A:
            element = A.pop()
            if element % 2!= 0:
                odd.append(element)
            else:
                even.append(element)
           even.append(odd.pop(0))
        return even + odd
        