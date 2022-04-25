from typing import List
import random
from collections import defaultdict

class Solution:

    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for i,num in enumerate(nums):
            self.pos[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.pos[target])