class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}
        for number in arr:
            if number in hash_map:
                hash_map[number] += 1
            else:
                hash_map[number] = 1
        result = []
        for value in list(hash_map.values()):
            if value in result:
                return False
            else:
                result.append(value)
        return True