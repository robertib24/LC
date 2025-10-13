class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def are_anagrams(s, t):
            if len(s) != len(t):
                return False
            
            count = {}
            for c in s:
                count[c] = count.get(c, 0) + 1
            
            for c in t:
                if c not in count:
                    return False
                count[c] -= 1
                if count[c] < 0:
                    return False
            
            return True
        
        result = [words[0]]
        
        for i in range(1, len(words)):
            if not are_anagrams(words[i-1], words[i]):
                result.append(words[i])
        
        return result
