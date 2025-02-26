#from scipy.special import pro_ang1

import random
def print_Fo():
    print('现在A，B要进行比赛。规则为：15回合制,每回合得15分获胜')
    print('A首先发球，若A赢一球则A发球，此时若A再赢一球，则积一分.\n否则B发球，若B赢球则B积一分，否则A发球')
def getInput():
    n=eval(input('\n请输入比赛场次:'))
    pro_A=eval(input('请输入A球员的能力值范围0-1:'))
    pro_B=eval(input('请输入B球员的能力值范围0-1:'))
    return n,pro_A,pro_B
def Gameend(sor_A,sor_B):
    return sor_A==15 or sor_B==15

def simOneGame(stat,pro_A,pro_B):
    sorA,sorB=0,0
    while not Gameend(sorA,sorB) :
        if stat=='A':
            if random.random()<=pro_A:
                sorA+=1
            else:
                stat='B'
        else:
            if random.random()<=pro_B:
                sorB+=1
            else:
                stat='A'
    return sorA,sorB


def simsGame(n,pro_A,pro_B):
    stat = 'A'
    win_A,win_B=0,0
    for i in range(n):
        sorA,sorB=simOneGame(stat,pro_A,pro_B)
        if sorA>sorB:
            win_A+=1
            stat='A'
        else :
            win_B+=1
            stat='B'
    return win_A,win_B

def print_Summary(n,win_A,win_B):
    print('A球员赢得场次{}，胜率为{:.1%}'.format(win_A,win_A/n))
    print('B球员赢得场次{}，胜率为{:.1%}'.format(win_B,win_B/n))
def main ():
    print_Fo()
    n,pro_A,pro_B=getInput()
    win_A,win_B=simsGame(n,pro_A,pro_B)
    print_Summary(n,win_A,win_B)
main()