f=1
sum=0
for i in range(1,967):
    sum+=f*i
    f=-f
print('{}'.format(sum))
