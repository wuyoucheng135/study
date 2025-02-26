count=0
def hannio(n,src,dst,mid):
    global count
    if n==1:
        print('{}:{}->{}'.format(1,src,dst))
        count+=1
    else:
        hannio(n-1,src,mid,dst)
        hannio(1,src,dst,mid)
        hannio(n-1,mid,dst,src)
hannio(4,'a','b','c')
print(count)