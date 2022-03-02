s='23'
num = int(s)
list = ['1','2','4','3']

f = lambda x:(int(x)-2,int(x))

print(min(list,key=f))
