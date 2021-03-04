class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        step = 0
        
        if num is 0:
            return 0;
        
        while num is not 1:
            if (num % 2 ==1):
                num = num-1;
            else:
                num = num / 2;
            step = step + 1;
            
        step = step + 1;
        return step;