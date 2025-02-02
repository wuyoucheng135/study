#摄氏温度和华氏温度之间的转换
temp=input('请输入温度摄氏度以C或c结尾，华氏度以F或f结尾:')
# if elif else 均以：结尾
if temp[-1] in ['c','C']:
#input输入的数据进行运算时，首先需要用eval将字符串转为代码执行，
#用temp[0:-1]来提取输入数据的数值部分
    f=eval(temp[0:-1])*1.8+32
    print('转换温度为{:.2f}f'.format(f))
elif temp[-1] in ['f','F']:
    c=(eval(temp[0:-1])-32)/1.8
    print('温度转换为{:.2f}c'.format(c))
else:
    print('输入格式错误')

