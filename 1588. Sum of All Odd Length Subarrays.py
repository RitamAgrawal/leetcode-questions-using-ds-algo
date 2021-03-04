class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Check for edge cases -- if !arr | if arr.length == 0:...
        add = 0
        if len(arr)==0:
            return add
        
        if len(arr)==1:
            return arr[0]              
        else:
            for i in range(len(arr)):
                add = arr[i] + add

            if len(arr)>1 and (len(arr)%2 == 1):
                add = sum(arr)+add      


            if len(arr)> 2:            
                for k in xrange(3,len(arr),2):
                    i = 0
                    while i+k <= len(arr):
                        add = sum(arr[i:i+k]) + add
                        i += 1
        return add

            