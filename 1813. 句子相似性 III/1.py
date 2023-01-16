#首先按空格划分为长短两个list
#两个指针分别指向短list的首位尾元素，然后进行首尾配对，
#有三种可能，1.从首部起可以全部匹配完，2.以尾部为末尾可以全部匹配完， 3.可以首位各匹配一部分
#一句话，短list必须是全匹配完的，也就是i>j为匹配完的状态。另外如果首尾都没有匹配，则即使在中间出现匹配也至少会出现两个段，不满足相似条件


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        listl,lists = (sentence1.split(' '),sentence2.split(' ')) if len(sentence1)>len(sentence2) else (sentence2.split(' '),sentence1.split(' '))
        i,j = 0,len(lists)-1
        lj  = len(listl)-1
        while i<len(lists) and lists[i]==listl[i]:
            i+=1
        if i>j:
            return True
        while j>=0 and lists[j]==listl[lj]:
            j-=1
            lj-=1
        if i>j:
            return True
        return False

x = Solution()
x.areSentencesSimilar("Eating right now","Eating")


