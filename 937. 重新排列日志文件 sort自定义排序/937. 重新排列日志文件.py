from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log:str) ->tuple:
            a,b = log.split(' ',1) #只从第一个空格分隔
            return (0,b,a) if b[0].isalpha() else (1,) #把每个分隔子串作为一个元组来比较，如果是字母日志元组首个元素为0，一定在数字日志前面
            #另外比较字母日志时内容的优先级比标识符高，所以b在元组中的位置在a前
        #元组排序print((1,2,3)<(0,1,2)) return False 从第一个元素开始比较，如果相同就比较下一个元素
        logs.sort(key=trans)
        return logs