class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if word.islower():
            return True
        if word.isupper():
            return True
        if word[0].isupper and word[1:].islower():
            return True
        return False