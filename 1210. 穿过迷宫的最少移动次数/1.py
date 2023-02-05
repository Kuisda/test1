#本质上是一种遍历
#bfs遍历，dist记录到达每个位置所需要的最短路径数，由于bfs的性质，第一次到达一个位置所得的路径长度一定是最小的，所以直接判断这个位置是否在dist中即可
#(x,y,status)三元组记录蛇此时的状态，这个是根据蛇尾来的，
from typing  import List
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        q=[(0,0,0)]
        n = len(grid)
        dist = {(0,0,0):0}
        while q:
            x,y,status = q.pop(0)
            if status==0:#横身状态
                #有向右，向下，顺时针旋转三种,其中顺时针旋转其实对应的x，y是一致的，但是对status有变化
                if y+2<n and grid[x][y+2]==0 and (x,y+1,0) not in dist:
                    dist[(x,y+1,0)]=dist[(x,y,0)]+1
                    q.append((x,y+1,0))
                if x+1<n and grid[x+1][y]==grid[x+1][y+1]==0 and (x+1,y,0) not in dist:
                    dist[(x+1,y,0)]=dist[(x,y,0)]+1
                    q.append((x+1,y,0))
                if x+1<n and y+1<n and grid[x+1][y]==grid[x+1][y+1]==0 and (x,y,1) not in dist:
                    dist[(x,y,1)] = dist[(x,y,0)]+1
                    q.append((x,y,1))
            else:#竖身状态
                #向右，向下，逆时针旋转
                if y+1<n and grid[x][y+1]==grid[x+1][y+1]==0 and (x,y+1,1) not in dist:
                    dist[(x,y+1,1)] = dist[(x,y,1)]+1
                    q.append((x,y+1,1))
                if x+2<n and grid[x+2][y]==0 and (x+1,y,1) not in dist:
                    dist[(x+1,y,1)] = dist[(x,y,1)]+1
                    q.append((x+1,y,1))
                if x+1<n and y+1<n and grid[x+1][y+1]==grid[x][y+1]==0 and (x,y,0) not in dist:
                    dist[(x,y,0)] = dist[(x,y,1)]+1
                    q.append((x,y,0))
        return dist.get((n-1,n-2,0),-1)#get如果找不到(n-1,n-2,0)就返回-1

