#https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]


class Solution:
    def mostWordsFound(self, sentences):
        
        
        max = 0
        
        for sent in sentences:
            words = len(sent.split())

            if max < words:
                max = words
        return max

        
        
                
        






result = Solution().mostWordsFound()
print(result)