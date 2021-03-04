class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output = []
        maximum_no_of_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] < maximum_no_of_candies:
                potential_no_of_candies = extraCandies + candies[i]
                if potential_no_of_candies >= maximum_no_of_candies:
                    output.append(True)
                else:
                    output.append(False)
            else:
                output.append(True)
        return output
