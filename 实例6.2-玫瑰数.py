for i in range(1000,10000):
    a=i%10
    b=int(i/10)%10
    c=int(i/100)%10
    d=int(i/1000)
    if pow(a,4)+pow(b,4)+pow(c,4)+pow(d,4)==i:
        print(i)
