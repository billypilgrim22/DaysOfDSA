class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d = {}
        ans = 0
        for i in range(len(words1)):
            if words1[i] not in d:
                d[words1[i]] = 1
            else:
                d[words1[i]] += 1
        
        for i in range(len(words1)):
            if(words1[i] in d):
                if(d[words1[i]] > 1):
                    d.pop(words1[i])
        
        for i in range(len(words2)):
            if(words2[i] in d):
                d[words2[i]] -= 1
                
        for key in d:
            if(d[key] == 0):
                ans += 1
                
        return ans