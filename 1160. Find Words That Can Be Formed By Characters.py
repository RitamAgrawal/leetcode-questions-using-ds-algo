class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count,good = 0, 0
        for word in words:
            for char in word:
                if chars.count(char)>= word.count(char):
                    good += 1
                else:
                    good = 0
                    break
            if good == len(word):
                count += good
            good = 0
        return count