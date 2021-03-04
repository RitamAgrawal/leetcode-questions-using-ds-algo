class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:       
        temp = sorted(nums)        
        head = 0
        tail = len(nums)-1        
        while head < tail:
            result = temp[head] + temp[tail]            
            if (result == target):
                head_idx = nums.index(temp[head])
                tail_idx = nums.index(temp[tail])
                if (head_idx == tail_idx):
                    tail_idx = nums.index(temp[tail], head_idx+1)
                return [head_idx, tail_idx]
            elif result < target:
                head += 1
            else:
                tail -= 1