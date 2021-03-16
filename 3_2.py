M = []
C = []
import random
a=0
for x in range (0,4,1):
    M = random.sample(range(0, 31), 4)
    print(M)
    C = M[a]
    a+=1
    print(C)
    
