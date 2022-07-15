#线段树主要用于区间和的修改以及查询。都可以做到O(nlogC),C在本题是10**9
#本题的本质就是给你一个区间，然后让你将其[start, end)内所有的元素值加上一，在进行了每一次的book更新的操作后，在返回[0, 1e9]这个区间内的最大元素值是多少。
from collections import defaultdict

class MyCalendarThree:
    def __init__(self):
        self.tree = defaultdict(int)#使用哈希表来表示线段树能够节省空间，只在访问某个下标时才创建该下标以及对应的节点值。
        self.lazy = defaultdict(int)

    def update(self,start:int,end:int,l:int,r:int,idx:int):
        #线段树，start，end是目标区间，l,r是当前搜索区间,idx表示的是当前节点对应在defaultdict中的位置
        #线段树中，非叶子节点表示的是其子树包含的所有叶子节点之和,就是区间和
        if end<l or start>r:#表示当前搜索区间在目标区间之外，直接返回
            return
        if start<=l and r<=end:#表示当前搜索区间在目标区间之内，说明该节点对应的搜索区间是目标区间的一部分
            self.tree[idx] +=1
            self.lazy[idx] +=1
        else:
            mid = (l+r) //2
            self.update(start,end,l,mid,idx*2)#idx*2对应当前节点的左子树在defaultdict中的位置
            self.update(start,end,mid+1,r,idx*2+1)#idx*2+1对应右子树
            self.tree[idx] = self.lazy[idx]+max(self.tree[idx*2],self.tree[idx*2+1])

    def book(self, start: int, end: int) -> int:
        self.update(start,end-1,0,10**9,1)
        return self.tree[1]