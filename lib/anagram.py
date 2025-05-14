# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        matches = []
        sorted_word = sorted(self.word)

        for candidates in candidates:
            if(len(candidates) == len(self.word) and candidates.lower() != self.word):
                if sorted(candidates.lower()) == sorted_word:
                    matches.append(candidates)
        return matches