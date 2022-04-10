from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mouse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        return len(set("".join(mouse[ord(ch)-ord('a')] for ch in word)for word in words))
        


