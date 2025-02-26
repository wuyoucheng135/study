f=open('hamlet.txt','r+')
ls=['w','y','c']
f.writelines(ls)
f.seek(0)
for line in f:
    print(line)
f.close()