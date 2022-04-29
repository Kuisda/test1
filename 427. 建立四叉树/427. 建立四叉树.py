class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
#简单的递归，判断全为1或0的方式是直接遍历
#如果不全为0,1，则把矩阵分为四个部分，进行递归
#dfs(r0,c0,r1,c1)使用左上角(r0,c0)和右下角(r1,c1)两个点来表示一个矩阵的位置
class Solution(object):
    def construct(self, grid):
        def dfs(r0,c0,r1,c1):
            if all(grid[i][j]==grid[r0][c0] for i in range(r0,r1) for j in range(c0,c1)):
                return Node(val=(grid[r0][c0]==1),isLeaf=True)
            else:
                return Node(
                    val=True,
                    isLeaf=False,
                    topLeft=dfs(r0,c0,(r0+r1)//2,(c0+c1)//2),
                    topRight=dfs(r0,(c0+c1)//2,(r0+r1)//2,c1),
                    bottomLeft=dfs((r0+r1)//2,c0,r1,(c0+c1)//2),
                    bottomRight=dfs((r0+r1)//2,(c0+c1)//2,r1,c1)
                )
        return dfs(0,0,len(grid),len(grid))

#使用二维前缀和，用来优化判断全0或全1的过程
#二维前缀和pre[i][j]表示的是以（i，j）为右下角的矩阵的数之和
#pre[i][j] = pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1]+grid[i-1][j-1]
class Solution(object):
    def construct(self, grid):
        n = len(grid)
        pre = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(1,n+1):
                pre[i][j] = pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1]+grid[i-1][j-1]
        def getSum(r0,c0,r1,c1):#利用前缀和求区间内的数之和
            return pre[r1][c1]-pre[r1][c0]-pre[r0][c1]+pre[r0][c0]
        def dfs(r0,c0,r1,c1):
            total = getSum(r0,c0,r1,c1)
            if  total ==0:
                return Node(val=False,isLeaf=True)
            elif total == (r1-r0)*(c1-c0):
                return Node(val=True,isLeaf=True)
            else:
                return Node(
                    val=True,
                    isLeaf=False,
                    topLeft=dfs(r0,c0,(r0+r1)//2,(c0+c1)//2),
                    topRight=dfs(r0,(c0+c1)//2,(r0+r1)//2,c1),
                    bottomLeft=dfs((r0+r1)//2,c0,r1,(c0+c1)//2),
                    bottomRight=dfs((r0+r1)//2,(c0+c1)//2,r1,c1)
                )
        return dfs(0,0,n,n)
