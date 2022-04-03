from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for ch in letters:
            if ch>target:
                return ch
        return letters[0]        

x = Solution()
x.nextGreatestLetter(["c","f","j"],"a")