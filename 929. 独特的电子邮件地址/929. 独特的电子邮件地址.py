from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def typeTurn(s:str)->str:
            slst = s.split('@')
            ch = slst[0]
            num = 0
            while 1:
                if ch=='+':
                    slst[0] = slst[0][0:num]
                elif ch=='.':
                    slst[0] = slst[0][0:num]+slst[0][num+1:]
                num+=1
                if num >=len(slst[0]):
                    break
                ch = slst[0][num]
            return slst[0]+'@'+slst[1]
        ans = set()
        for s in emails:
            ss = typeTurn(s)
            ans.add(ss)
        return len(ans)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            i = email.index('@')
            local = email[:i].split('+', 1)[0]  # 去掉本地名第一个加号之后的部分
            local = local.replace('.', '')  # 去掉本地名中所有的句点
            emailSet.add(local + email[i:])
        return len(emailSet)
        

