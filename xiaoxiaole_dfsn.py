from matplotlib import artist
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy

'''
功    能 : 消消乐实验回溯法图形演示
输    入 : m*n的矩阵，mat[i][j] 表示 (i,j) 位置的颜色
输    出 : 图形颜色结果（包含回溯过程）
'''

'''
sample input: 
样例输入:
3 3 4 3 1 2 3 
3 2 3 3 3 2 3 
2 4 3 4 3 1 1
1 3 4 3 4 4 3
3 3 1 1 3 1 1
3 4 3 3 4 3 3
1 4 4 3 3 2 3
'''

colors = ['white', 'red', 'blue', 'yellow', 'black']
k, m, n, x = 4, 6, 6, 3 ## m, n are wide -1 
artists = []

'''
function  : getCir 得到所有圆的artist对象
param mat : 棋盘数组
return    : 所有圆的artist对象(list[])
'''


def getCir(mat):
    fr = []
    for i in range(m):
        for j in range(n):
            fr += plt.plot(j * 10 + 40, 80 - i * 10, "o", color=colors[mat[i][j]], markersize=19)
    return fr


# 绝对值
def iabs(x):
    if x < 0:
        return -x
    return x


# 打印矩阵
def printm(mat):
    for i in range(m):
        for j in range(n):
            print(mat[i][j], ' ', end='')
        print()
    print()


# 根据坐标在frame帧上绘制矩形
def getRectangle(frame, x1, y1, x2, y2, c):
    frame += plt.plot([x1, x2], [y1, y1], color=c)
    frame += plt.plot([x1, x2], [y2, y2], color=c)
    frame += plt.plot([x1, x1], [y1, y2], color=c)
    frame += plt.plot([x2, x2], [y1, y2], color=c)
    return frame


'''
function  : erase 消去方块并且使方块下落
param mat : 棋盘数组的引用
return    : 消去后增加的得分
'''


def erase(mat,color):
    cnt3, cnt4, cnt5 = 0, 0, 0
    # 计算3，4，5的连续块个数
    ## idea: if mat duplicate and mat == typical colors then we will add a combo reward
    color_b=0
    botom_b=0
    for i in range(m): ## hang 
        for j in range(n): ## lie 
            botom_b= 1*i
            if mat[i][j]==color:
                print('bonus color',mat[i][j])
                color_b+=1
            if i + 2 < m and mat[i][j] != 0:
                if (iabs(mat[i][j]) == iabs(mat[i + 1][j]) and
                        iabs(mat[i + 1][j]) == iabs(mat[i + 2][j])):
                    mat[i][j] = -iabs(mat[i][j])
                    mat[i + 1][j] = -iabs(mat[i][j])
                    mat[i + 2][j] = -iabs(mat[i][j])
                    cnt3 += 1  ## we can add the combo reward here
            if j + 2 < n and mat[i][j] != 0:
                if (iabs(mat[i][j]) == iabs(mat[i][j + 1]) and
                        iabs(mat[i][j + 1]) == iabs(mat[i][j + 2])):
                    mat[i][j] = -iabs(mat[i][j])
                    mat[i][j + 1] = -iabs(mat[i][j])
                    mat[i][j + 2] = -iabs(mat[i][j])
                    cnt3 += 1
            if i + 3 < m and mat[i][j] != 0:
                if (iabs(mat[i][j]) == iabs(mat[i + 1][j]) and
                        iabs(mat[i + 1][j]) == iabs(mat[i + 2][j]) and
                        iabs(mat[i + 2][j]) == iabs(mat[i + 3][j])):
                    mat[i][j] = -iabs(mat[i][j])
                    mat[i + 1][j] = -iabs(mat[i][j])
                    mat[i + 2][j] = -iabs(mat[i][j])
                    mat[i + 3][j] = -iabs(mat[i][j])
                    cnt4 += 1
            if j + 3 < n and mat[i][j] != 0:
                if (iabs(mat[i][j]) == iabs(mat[i][j + 1]) and
                        iabs(mat[i][j + 1]) == iabs(mat[i][j + 2]) and
                        iabs(mat[i][j + 2]) == iabs(mat[i][j + 3])):
                    mat[i][j] = -iabs(mat[i][j])
                    mat[i][j + 1] = -iabs(mat[i][j])
                    mat[i][j + 2] = -iabs(mat[i][j])
                    mat[i][j + 3] = -iabs(mat[i][j])
                    cnt4 += 1
            if i + 4 < m and mat[i][j] != 0:
                if (iabs(mat[i][j]) == iabs(mat[i + 1][j]) and
                        iabs(mat[i + 1][j]) == iabs(mat[i + 2][j]) and
                        iabs(mat[i + 2][j]) == iabs(mat[i + 3][j]) and
                        iabs(mat[i + 3][j]) == iabs(mat[i + 4][j])):
                    mat[i][j] = -iabs(mat[i][j])
                    mat[i + 1][j] = -iabs(mat[i][j])
                    mat[i + 2][j] = -iabs(mat[i][j])
                    mat[i + 3][j] = -iabs(mat[i][j])
                    mat[i + 4][j] = -iabs(mat[i][j])
                    cnt5 += 1
            if j + 4 < n and mat[i][j] != 0:
                if (iabs(mat[i][j]) == iabs(mat[i][j + 1]) and
                        iabs(mat[i][j + 1]) == iabs(mat[i][j + 2]) and
                        iabs(mat[i][j + 2]) == iabs(mat[i][j + 3]) and
                        iabs(mat[i][j + 3]) == iabs(mat[i][j + 4])):
                    mat[i][j] = -iabs(mat[i][j])
                    mat[i][j + 1] = -iabs(mat[i][j])
                    mat[i][j + 2] = -iabs(mat[i][j])
                    mat[i][j + 3] = -iabs(mat[i][j])
                    mat[i][j + 4] = -iabs(mat[i][j])
                    cnt5 += 1
    # 方块下落
    for j in range(n):
        st = m - 1
        while st >= 0 and mat[st][j] > 0:
            st -= 1
        ed = st
        while ed >= 0 and mat[ed][j] <= 0:
            ed -= 1
        delta = st - ed
        for i in range(ed, -1, -1):
            mat[i + delta][j] = mat[i][j]
            mat[i][j] = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] < 0:
                mat[i][j] = 0
    # 消去重复的计数
    cnt4 -= 2 * cnt5
    cnt3 -= (3 * cnt5 + 2 * cnt4)
    if cnt3 + cnt4 * 4 + cnt5 * 10 == 0:
        return 0
    return cnt3 + cnt4 * 4 + cnt5 * 10 + botom_b + color_b+erase(mat,color) ## why 4 and 10? seems arbitrary 


'''
function   : dfs_tpk
param mat  : 消消乐棋盘矩阵 
param step : 当前递归树的深度
param sum  : 当前得分和
param tpk  : 选取前 tpk 大的分支进行递归
return     : ----
'''


def dfs_tpk(mat, step, sum, tpk,color):
    if step == 0:
        return
    seq = []
    # 消去检测，获得所有分支
    for i in range(m): ## m is how depth is the rectrangle
        for j in range(n):
            if i + 1 < m and mat[i][j] > 0 and mat[i + 1][j] > 0:
                # print(mat[i][j])
                a = copy.deepcopy(mat)
                a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j] ## why?
                res = erase(a,color)
                if res > 0:
                    seq.append([res, i, j, i + 1, j])
            if j + 1 < n and mat[i][j] > 0 and mat[i][j + 1] > 0:
                a = copy.deepcopy(mat)
                a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
                res = erase(a,color)
                if res > 0:
                    seq.append([res, i, j, i, j + 1])
    # print('seq',seq)
    # 按照得分排序
    for i in range(seq.__len__()):
        for j in range(seq.__len__() - 1):
            if seq[j][0] < seq[j + 1][0]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    # 递归tpk大的分支
    for i in range(min(seq.__len__(), tpk)):
        a = copy.deepcopy(mat)
        artists.append(getCir(a))
        # 打印矩形框同时打印方块们
        x1, y1, x2, y2 = seq[i][1], seq[i][2], seq[i][3], seq[i][4]
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        y1 -= 0.5
        y2 += 0.5
        x1 -= 0.5
        x2 += 0.5
        artists.append(getRectangle(getCir(a), y1 * 10 + 40, 80 - x1 * 10, y2 * 10 + 40, 80 - x2 * 10, 'red'))
        a[seq[i][1]][seq[i][2]], a[seq[i][3]][seq[i][4]] = a[seq[i][3]][seq[i][4]], a[seq[i][1]][seq[i][2]]
        artists.append(getRectangle(getCir(a), y1 * 10 + 40, 80 - x1 * 10, y2 * 10 + 40, 80 - x2 * 10, 'blue'))
        # 消除方块，递归
        res = erase(a,color)
        ## the res score is used to decide how to erase
        dfs_tpk(a, step - 1, sum + res, tpk,color)
        # print('score',sum+res) ## what is the meaning of score?
        # print('juzhen',a)
        # print('step', step-1)
        # 回溯打印
        artists.append(getCir(a))


if __name__ == '__main__':

    # mat = []
    # for i in range(m):
    #     mat.append(list(map(int, input().split(" "))))
    ## change new format of input

    mat=[[3, 3, 4, 3, 4, 2, 1], [3, 2, 3, 3, 2, 1, 2], [2, 4, 3, 4, 3, 3, 1], [1, 3, 4, 3, 1, 1, 5], [3, 3, 1, 1, 2, 1, 2], [3, 4, 3, 3, 3, 4, 2], [1, 4, 4, 3, 2, 2, 3]]  
    '''
    for i in range(m):
        for j in range(n):
            print(mat[i][j], end='')
        print()
    '''
    color=2
    fig = plt.figure()
    plt.xlim(-10, 140)
    plt.ylim(-10, 100)

    dfs_tpk(mat, 8, 0, 3,color) ## if it is very deep the program will stuck

    ain = animation.ArtistAnimation(fig=fig, artists=artists, interval=1000)
    plt.show()
    ain.save(f'demo{color}.gif', fps=2)
