def f(n):
    if n in [1,2]:
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(eval(input())))