from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        ans = []
        minindex = 2001
        for n,s in enumerate(list1):
            dic[s] = n
        for n,s in enumerate(list2):
            if s in dic:
                if n+dic[s]==minindex:
                    ans.append(s)
                elif n+dic[s]<minindex:
                    minindex = n+dic[s]
                    ans = [s]    
        return ans        


