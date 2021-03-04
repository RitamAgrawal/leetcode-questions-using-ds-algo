class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hash_map = {"a":".-",
                    "b":"-...",
                    "c":"-.-.",
                    "d":"-..",
                    "e":".",
                    "f":"..-.",
                    "g":"--.",
                    "h":"....",
                    "i":"..",
                    "j":".---",
                    "k":"-.-",
                    "l":".-..", 
                    "m":"--",
                    "n":"-.",
                    "o":"---",
                    "p":".--.",
                    "q":"--.-", 
                    "r":".-.", 
                    "s":"...", 
                    "t":"-", 
                    "u":"..-",
                    "v":"...-",
                    "w":".--",
                    "x":"-..-",
                    "y":"-.--",
                    "z":"--.."
                   }
        transformation = []
        output = 0
        
        for word in words:
            new_string = ""
            for i in range(len(word)):
                new_string += hash_map[word[i]]
            if new_string not in transformation:
                transformation.append(new_string)
        
        return len(transformation)
        