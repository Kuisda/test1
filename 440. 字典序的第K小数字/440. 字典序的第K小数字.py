#字典树搜索问题，按照字典序找到第t个，也就是对字典树先序遍历
class Solution:
    def getCnt(self,x:int,limit:int)->int: #计算前缀为x的数字在[1,limit]中的数量
        steps,first,last = 0,x,x
        while first <=limit:#一层一层的加，first指向该层最左边节点，last指向该层最右边节点，直到该层最左边节点都比上界limit大时结束
            steps+=min(last,limit) - first+1 #limit所在层最右结点是limit而不是last
            first*=10
            last = last*10+9
        return steps


    def findKthNumber(self, n: int, k: int) -> int:
        ans = 1
        while k>1:
            cnt = self.getCnt(ans,n)
            if cnt<k:   #cnt<k说明要找的目标前缀在ans后面
                k-=cnt  
                ans+=1
            else:
                k-=1    #跳过ans本身，所以计数-1
                ans*=10 #从ans作为前缀的第一个(最小的)开始（进入字典树的下一层）
        return ans            