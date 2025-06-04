class Solution(object):
    def answerString(self, word, numFriends):
        if numFriends == 1:
            return word
        m = len(word)-(numFriends-1)
        c = max(word)
        return max(word[i:i+m] for i in range(len(word)) if word[i] == c)
