class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = max(nums)
        index = nums.index(m1)
        nums.pop(index)
        m2 = max(nums)
        return ((m1-1)*(m2-1))