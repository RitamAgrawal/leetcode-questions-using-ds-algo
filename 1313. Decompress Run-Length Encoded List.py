class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = []
        for i in range(0, len(nums)/2):
            array += nums[2*i] * [nums[(2*i)+1]]
        return array
            
    