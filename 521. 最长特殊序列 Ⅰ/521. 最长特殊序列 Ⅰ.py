#如果a==b则任意子序列公有，返回-1
#如果a!=b，a和b由于并不相同，所以可以选择其中较长一个作为最长子序列
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a),len(b)) if a!=b else -1