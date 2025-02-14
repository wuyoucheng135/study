for i in range(100,1000):
    a=i%10
    b=int(i/10)%10
    c=int(i/100)%10
    if pow(a,3)+pow(b,3)+pow(c,3)==i:
        print(i,end=',')
