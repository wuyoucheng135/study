from random import random
from time import perf_counter
DARTS=pow(1000,5)
numbers=0
start=perf_counter()    
for i in range(DARTS):
    x,y=random(),random()
    if pow(x**2+y**2,0.5)<1.0:
        numbers+=1
pi=numbers/DARTS*4
dur=perf_counter() - start
print('pi的值是：{} 运行时间是：{}'.format(pi,dur))
