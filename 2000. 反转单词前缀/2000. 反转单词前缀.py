class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pos = 0
        i = word.find(ch) + 1
        """
        for i in range(len(word)):
            if word[i]==ch:
                pos = i
                break
        """    
        ans = word[pos::-1]+word[pos+1::]
        return ans        
