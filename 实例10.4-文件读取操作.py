f=open('date.txt','r+')
for line in f:
    print(line,type(line))
f.close()