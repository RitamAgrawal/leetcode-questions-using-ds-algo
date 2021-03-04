class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        dictionary = {}
        
        if len(s) != len(indices):
            return "invalid"
        
        for i in range(len(s)):
            dictionary[indices[i]] = s[i]
        return "".join(dictionary.values())
        