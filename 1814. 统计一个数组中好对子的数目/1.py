#题目给的关系式：nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])两边都是二者的关系
#但其实把同种变量都归到一边就可以实现关系式都是同种元素，这样就减少了对比次数，只用看nums[i]-rev(nums[j])是否一样
from typing import List
from collections import Counter
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        cnt = Counter()
        ans = 0
        for num in nums:
            rev = int(str(num)[::-1])
            ans+= cnt[num-rev] #每多出一个(num-rev)，它与其中的所有对都能进行一次配对，所以配对次数增加这么多
            cnt[num-rev]+=1
        return ans % (10 ** 9 + 7)
