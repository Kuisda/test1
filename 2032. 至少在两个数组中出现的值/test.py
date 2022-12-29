from collections import defaultdict


ans = set()
ans.add(1)
ans.add(2)
print("ans:",type(ans),"turn:",type(list(ans)))



mask = defaultdict(int)
mask[1]='a'
mask[2]='b'
print("items:",mask.items())