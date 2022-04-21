class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        wordlist= sentence.split(' ')
        n = len(wordlist)
        vowel = ['a','e','i','o','u']
        ans=''
        for num,s in enumerate(wordlist):
            if s[0].lower() in vowel:
                s+='ma'
            else:
                ch = s[0]
                s = s[1:]+ch+'ma'
            s+='a'*(num+1)
            ans+=s+' ' if num!=n-1 else s
        return ans

x = Solution()
x.toGoatLatin("Each word consists of lowercase and uppercase letters only")