from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for aster in asteroids:
            negAlive = True
            if aster>0:
                stack.append(aster)
            while negAlive and aster<0 and stack and stack[-1]>0:
                negAlive = stack[-1]<-aster #负向行星碰撞后是否存活
                if stack[-1]<=-aster:#负向行星与最靠近的正向行星碰撞后正向行星是否存活
                    stack.pop()
            if negAlive and aster<0:
                stack.append(aster)
        return stack

#小优化：Alive同时表示正向是否存活，然后在append中就可以直接判断alive
def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for aster in asteroids:
            alive = True
            while alive and aster < 0 and st and st[-1] > 0:
                alive = st[-1] < -aster
                if st[-1] <= -aster:
                    st.pop()
            if alive:
                st.append(aster)
        return st




x = Solution()
x.asteroidCollision([5,10,-5])



