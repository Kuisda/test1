from collections import deque
#每一次遍历就是将队列首部放到尾部，k-1次后去掉遍历到的第k个数
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(range(1,n+1))
        while len(q)>1:
            for _ in range(k-1):
                temp = q.popleft()
                q.append(temp)
            q.popleft()
        return q.pop()

class Solution1:
    def findTheWinner(self, n: int, k: int) -> int:
        return 1 if n == 1 else (k + self.findTheWinner(n - 1, k) - 1) % n + 1


class Solution2:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 1
        for i in range(2, n + 1):
            winner = (k + winner - 1) % i + 1
        return winner
