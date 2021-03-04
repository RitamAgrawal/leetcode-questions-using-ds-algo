from operator import mul

class Solution(object):
    def subtractProductAndSum(self, num):        
        """
        :type n: int
        :rtype: int
        """        
        result = [int(x) for x in str(num)]
        product = reduce(mul,result,1)
        difference = product - sum(result)
        return difference
        