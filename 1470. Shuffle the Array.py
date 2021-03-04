class Solution(object):
    def shuffle(self, nums, mid):
        """
        :type nums: List[int]
        :type mid: int
        :rtype: List[int]
        """
        mid = len(nums) // 2
        first_half=[]
        for i in range(mid):  # middle term is exclusive
            first_half.append(nums[i])
        second_half=[]
        for i in range(mid,len(nums)):
            second_half.append(nums[i])
        output=[]
        for i in range(mid):
            output.append(a[i])
            output.append(b[i])
        return output

        