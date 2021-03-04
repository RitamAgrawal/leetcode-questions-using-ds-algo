class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            return [-1]
        max_ = max(arr[1:])
        for i in range(len(arr)-1):
            if arr[i] >= max_:                
                max_ = max(arr[i+1:])
            arr[i] = max_
        arr.pop()
        arr.append(-1)
        return arr
        
                
                
        