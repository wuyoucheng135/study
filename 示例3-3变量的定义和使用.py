luck_number=8#整形变量定义
my_name='吴友成'#字符串类型变量定义
print('luck_number的数据类型是:',type(luck_number),sep='')
print(my_name,'的幸运数字是:',luck_number,sep='')

#python动态修改变量的数据类型，通过赋予不同的类型的值可以直接修改
luck_number='北京欢迎你'
print('luck_number的数据类型是:',luck_number)

#python中允许多个变量指向同一个值
no=number=1024
print(no,number)
print(id(no),id(number))