class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        moves = 0
        for i in range(len(points)-1):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[i+1][0]
            y2 = points[i+1][1]
            moves += max(abs(x1-x2), abs(y1-y2))
        return moves