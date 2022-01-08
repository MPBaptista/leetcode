class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum_words  = 0
        for sentence in sentences:
            if len(sentence.split()) > maximum_words:
                maximum_words = len(sentence.split())
        return maximum_words
        