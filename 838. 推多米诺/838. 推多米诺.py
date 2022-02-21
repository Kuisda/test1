from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        q = deque()
        time = [-1]*n
        force = [[] for _ in range(n)]
        for i,f in enumerate(dominoes):
            if f!='.':
                q.append(i)
                time[i]=0
                force[i].append(f)
        
        res = ['.']*n
        while q:
            i = q.popleft()
            if len(force[i])==1:
                res[i] = f = force[i][0]
                ni =i-1 if f=='L' else i+1 #传导受力，这里只记录传导一格
                if 0<=ni<n:
                    t = time[i]
                    if time[ni]== -1:
                        q.append(ni)
                        time[ni] = t+1
                        force[ni].append(f)
                    elif time[ni] == t+1: #在力作用到的同一时间另一侧的力也作用到，所以是两侧力，该位置力不再传导
                        force[ni].append(f)
        return ''.join(res)                            

