class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = []
        for i in range(n):
            nums.append(start + 2*i)
        result = reduce(lambda x,y:x^y, nums)
        return result
        