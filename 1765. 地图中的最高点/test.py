import numpy as np
from queue import Queue
isWater = [[0,1],[0,0],[1,1]]
matrix = np.array(isWater)
print(matrix+1)
print(len(isWater))


q = Queue()

q.put((1,2,3))

a,b,c = q.get()
print(a,b,c)
