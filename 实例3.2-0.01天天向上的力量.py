facker=0.005
dayup=1
daydown=1
for i in range(365):
    dayup*=1+facker
    daydown*=1-facker
print('dayup{:.3f}\ndaydown{:.3f}'.format(dayup,daydown))
facker=0.01
dayup=1
daydown=1
for i in range(365):
    dayup*=1+facker
    daydown*=1-facker
print('dayup{:.3f}\ndaydown{:.3f}'.format(dayup,daydown))