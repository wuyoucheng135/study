import time
scale=50
start=time.perf_counter()
print('执行开始'.center(25,'-'))
for i in range(scale+1):
    a=i/scale*100
    b='*'*i
    c='-'*(scale-i)
    dur=time.perf_counter()-start
    print('\r{:>2.0f}%[{}->{}]{:.2f}s'.format(a,b,c,dur),end='')
    time.sleep(0.3)
print('\n','执行结束'.center(25,'-'))