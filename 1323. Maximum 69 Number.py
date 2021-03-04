class Solution:
    def maximum69Number (self, num: int) -> int:
        new_string = ""
        string = str(num)
        if "6" in string:
            split_i = string.index("6")
            new_string += string[:split_i]+"9"+string[split_i+1:]
            return int(new_string)
        else:
            return num
        