s='1,2,3,4'
def rvs(s):
    if s=='':
        return s
    else:
        return rvs(s[1:])+s[0]
print(rvs(s))