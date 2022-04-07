class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            ss = s[i+1:n]+s[0:i+1]
            if ss==goal:
                return True
        return False        
#return len(s) == len(goal) and goal in s + s 如果goal是s翻转的结果，goal一定是s+s的子串