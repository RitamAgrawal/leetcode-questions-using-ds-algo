class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "L":
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                count +=1
        return count