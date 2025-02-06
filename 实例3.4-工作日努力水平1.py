def dayUP(args):
    dayup=1
    for i in range(365):
        if i%7 in [6,0]:
            dayup*=1-0.01
        else:
            dayup*=1+args
    return dayup
dayfactor=0.01
while(dayUP(dayfactor)<37.78):
    dayfactor+=0.01
print('工作日进步{:.2f}'.format(dayfactor))