class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        string = []
        new_string = "" 
        for s in S:
            new_string += s
            if new_string.count("(") == new_string.count(")"):                
                string.append(new_string)
                new_string = "" 
        while string:
            sub = string.pop(0)
            if sub != "":
                new_string += sub[1:-1]
            else:
                new_string = ""
        return new_string
        