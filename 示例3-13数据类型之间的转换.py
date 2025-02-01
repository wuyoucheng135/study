x=10
y=3
z=x/y   #隐式转换，通过计算将int转为folat
print(z,type(z))

#将folat转为int类型，只保留整数部分
print('folat转为int类型',int(3.14))
print('folat转为int类型',int(3.94))

#将int转为folat类型，只保留整数部分
print('int转为folat类型',float(3))
print('int转为folat类型',float(300))

#将str转成int or float类型
print(int('0x567a',16)) #将十六进制字符串转为十进制数并输出
print(int('567'))       #将是十进制字符转为十进制数值

#chr ord 一对
print(ord('吴'))        #ord('吴')将字转为数值
print(chr(25578))       #chr(3244)将数值转为字

