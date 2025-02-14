import random as r
r.seed(123)
DARTS=eval(input())
numbers=0
for i in range(DARTS):
    x,y=r.random(),r.random()
    if pow(x,2)+pow(y,2)<1:
        numbers+=1
pi=numbers/DARTS*4
print('{:6f}'.format(pi))