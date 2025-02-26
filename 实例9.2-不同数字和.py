def getNumber():
    numbers = []
    while True:
        num_str = input('请输入数字（输入结束直接回车）: ')
        if num_str == '':  # 直接回车退出
            break
        num = float(num_str)  # 更安全的类型转换
        numbers.append(num)
    return numbers

def main():
    different_numbers = set(getNumber())
    total = sum(different_numbers)  # 直接使用内置sum函数
    print("去重后的数字总和为:", total)

main()