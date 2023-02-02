q = [1,2,3]
print(q.pop(0))
print(q)

q.append(4)
print(q)
print([-1 for _ in range(3)])



print(list(map(lambda x, y: x if x>y else y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))