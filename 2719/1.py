from functools import cache
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def calc(s :str)->int:
            @cache
            def dfs(i :int, sum :int,is_limit :int)->int:
                if sum > max_sum:
                    return 0
                if i == len(s):
                    return sum >= min_sum #1 or 0
                res = 0
                up = int(s[i]) if is_limit else 9
                for j in range(up+1):
                    res += dfs(i+1,sum + j ,is_limit and j==up)
                return res
            return dfs(0,0,True)
        judge_num1 = min_sum <= sum(map(int,num1))<= max_sum
        return (calc(num2) - calc(num1)+judge_num1) % 1000000007
        

c = Solution()
c.count("1","12",1,8)           

