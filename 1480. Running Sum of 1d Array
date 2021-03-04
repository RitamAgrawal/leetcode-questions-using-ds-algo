class Solution(object):
    def runningSum(self, given_array):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array_of_array = [given_array[0]]
        for j in range(1,len(given_array)):
            add = given_array[j] + array_of_array[j-1]
            array_of_array.append(add)
        return array_of_array
