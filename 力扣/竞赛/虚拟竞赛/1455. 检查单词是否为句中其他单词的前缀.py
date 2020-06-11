class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence_slice = sentence.split()
        for index in range(len(sentence_slice)):
            if sentence_slice[index].startswith(searchWord):
                return index + 1
        return -1