from secrets import choice
#集合的查询不是o(1)
#哈希表可以在o(1)完成插入和删除
#变长数组可以满足o(1)获取随机元素操作,另外数据的pop操作能在o(1)时间里完成删去尾部元素
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.dir = {}

    def insert(self, val: int) -> bool:
        if val in self.dir:
            return False
        self.dir[val] = len(self.nums) #val对应的值是val在nums中的位置
        self.nums.append(val)    
        return True
    def remove(self, val: int) -> bool:
        if val not in self.dir:
            return False
        #这里主要完成的操作就是把要删除的val与nums末尾数据交换然后删掉nums末尾数据，注意nums原末尾数据由于位置变了所以在dir中也需要更改
        id = self.dir[val] #val 在 nums中的pos
        self.nums[id] = self.nums[-1]
        self.dir[self.nums[id]] = id #修改原来在nums末尾处的值tempVal在dir中的值(也就是tempVal在nums中的新位置(就是val在nums中的位置))
        self.nums.pop()        
        del self.dir[val]
        return True

    def getRandom(self) -> int:
        return choice(self.nums)