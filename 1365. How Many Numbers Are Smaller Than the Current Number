class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums, output: List[int]
        :rtype: List[int]
        """
        output = []                   
        for current_index in range(len(nums)):
            count = 0
            for index in range(len(nums)):
                if ((index != current_index) and nums[index] < nums[current_index]):
                    count+= 1
            output.append(count)
        return output
        