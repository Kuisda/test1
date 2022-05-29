class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            slist = queryIP.split('.')
        else:
            slist = queryIP.split(':')
        n = len(slist)
        if n==4: #每个按'.'分隔的区间不能为空，不能有前导零，不能有除了set_4以外的符号，且如果能化为整型，数值要在[0.255]之间
            set_4 = ('0','1','2','3','4','5','6','7','8','9')
            for i,s in enumerate(slist):
                if len(s)>1 and s[0]=='0' or len(s)==0:
                    return "Neither"
                for j,ch in enumerate(s):
                    if ch not in set_4:
                        return "Neither"
                if int(s)<0 or int(s)>255:
                    return "Neither"
            return "IPv4"
        elif n==8:#每个按':'分隔的区间不能有set外的符号，长度在[1,4]之间
            set = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F')
            for i,s in enumerate(slist):
                if len(s)<1 or len(s)>4:
                    return "Neither"
                for j,ch in enumerate(s):
                    if ch not in set:
                        return "Neither"
            return "IPv6"
        else:
            return "Neither"

x = Solution()
x.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")
                
                
