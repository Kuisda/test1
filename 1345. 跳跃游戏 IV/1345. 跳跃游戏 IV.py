from typing import List
from collections import defaultdict
from collections import deque

#广度优先搜索，在遍历过一遍后删除值相同带来的路径，防止同值内的各个idx交叉访问
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        idxSameValue = defaultdict(list)
        for i,a in enumerate(arr):
            idxSameValue[a].append(i) #dict value:[idx1,idx2...]
        idxVisit = set()
        q = deque()
        q.append([0,0])
        idxVisit.add(0)

        while q:
            idx,step = q.popleft()
            if idx == len(arr)-1:
                return step
            v = arr[idx]
            step+=1
            for i in idxSameValue[v]:
                if i not in idxVisit:
                    idxVisit.add(i)
                    q.append([i,step])
            del idxSameValue[v]         #该值对应的所有结点都访问过了，删除通过值相同形成的路径，防止重复判断

            if idx+1 <len(arr) and (idx+1) not in idxVisit:
                idxVisit.add(idx+1)
                q.append([idx+1,step])
            if idx-1 >= 0 and (idx-1) not in idxVisit:
                idxVisit.add(idx-1)
                q.append([idx-1,step])


