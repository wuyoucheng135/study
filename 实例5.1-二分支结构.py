#<表达式> if <条件> else <表达式>
#只能填充表达式而不能填带有等号的语句
guess=eval(input())
print('{}'.format(99 if guess==99 else 0))