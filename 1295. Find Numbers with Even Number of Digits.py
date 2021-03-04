class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        output = 0
        if len(nums) == 0:
            return output
        for num in nums:
            x = num
            count = 0
            while x>=1:
                x = x / 10
                count += 1
            if count % 2 == 0:
                output += 1
        return output
            
        