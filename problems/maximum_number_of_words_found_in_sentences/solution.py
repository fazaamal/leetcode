class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max=0
        for i in sentences:
            if(i.count(' ') > max):
                max = i.count(' ')
        
        return max+1