for i in range(3):
    name=input()
    keys=input()
    if name=='Kate' and keys=='666666':
        print('登录成功！')
        break
else:
    print('3次用户名或者密码均有误！退出程序。')