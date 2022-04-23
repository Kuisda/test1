#核心目标是求一个凸包
# Jarvis 算法
#从任意一个点开始，找到从该点开始另一个点结束的向量使得其余的所有点都在这个向量的左边(右边也可，就是后面的也都要找右边的)
#然后从这个向量的头部的点开始再找另一个点f形成指向f的向量，要求所有其余的点都在这个向量的左边
#直到找到的是最初的点结束。
from typing import List
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        #当pq x qr >0时，说明r点在向量pq的左侧
        
        def cross(p:List[int],q:List[int],r:List[int]) -> int: #二维向量叉乘 pq(x1,y1) x qr(x2,y2) = x1y2-x2y1
            return (q[0]-p[0])*(r[1]-q[1])-(q[1]-p[1])*(r[0]-q[0])
    

        n = len(trees)
        if n<=3:
            return trees
        
        leftmost = 0 #选用在x轴上最左边的点为初始点
        for i,tree in enumerate(trees):
            if tree[0] < trees[leftmost][0]:
                leftmost = i
        
        ans = []
        vis = [False]*n
        p = leftmost
        while True:
            q = (p+1)%n #顺序的遍历所有向量头部
            for r,tree in enumerate(trees):
                #当叉积小于0说明r在pq的右侧，用pr来代替之前的pq，这样就能确保最终的结果pq一定在所有点的右侧
                if cross(trees[p],trees[q],tree) <0:
                    q=r
                #检查有没有和向量pq在同一直线上的点i，如果有，i也可以视为在pq左侧,且它是在边界上的
            for i,v in enumerate(vis):
                if not v and i!=p and i!=q and cross(trees[p],trees[q],trees[i]) ==0:
                    ans.append(trees[i])
                    vis[i] = True
            if not vis[q]:
                ans.append(trees[q])
                vis[q] = True
            p = q
            if p ==leftmost:
                break
        return ans
