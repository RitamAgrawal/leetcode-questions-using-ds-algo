class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = []
        source.append([paths[y][0] for y in range(len(paths))])
        
        for path in paths:
            if path[1] not in source[0]:
                return path[1]
                
        