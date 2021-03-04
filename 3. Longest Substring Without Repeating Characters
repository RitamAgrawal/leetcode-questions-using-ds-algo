class Solution:
    no_of_char = 256
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = [-1] * 256
        n = len(s)
        i, res = 0, 0
        for j in range(0,n):
            i = max(i,last_index[ord(s[j])]+1)
            res = max(res, j-i+1)
            last_index[ord(s[j])] = j
        return res