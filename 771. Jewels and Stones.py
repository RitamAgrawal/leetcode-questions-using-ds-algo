class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewelCount = 0
        stone_Count = {}
        for stone in S:
            if (stone in stone_Count):
                stone_Count[stone]+= 1
            else:
                stone_Count[stone] = 1
        for jewel in J:
            if (jewel in stone_Count):
                jewelCount+= stone_Count[jewel]
        return jewelCount
        