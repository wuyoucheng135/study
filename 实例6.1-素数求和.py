sums=0
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sums+=i
print(sums)

