facker=0.01
dayup=1
for i in range(365):
    if i%7 in [0,6]:
        dayup=dayup
    else:
        dayup*=1+facker
print('工作日进步休息日不进步dayup{:.3f}'.format(dayup))
facker=0.01
dayup=1
for i in range(365):
    if i%7 in [0,6]:
        dayup=dayup*(1-facker)
    else:
        dayup*=1+facker
print('工作日进步休息日退步dayup{:.3f}'.format(dayup))