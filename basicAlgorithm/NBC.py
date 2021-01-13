# 朴素贝叶斯推荐算法的实现
import numpy as np


def show(grade):
    print('*' * 5 + "朴素贝叶斯推荐算法展示前四位用户推荐结果前两甲及评分" + '*' * 5)
    for i in range(len(grade)):
        print('*'*5 + "第{:d}位用户".format(i + 1) + '*'*5)
        for j in range(len(grade[i])):
            if j < 20:
                print("电影编号:{:d}".format(int(grade[i][j][0])))
                print("推荐评分:{:.4f}".format(grade[i][j][1]))
    return


def saveGrade(grade, num):
    with open('saveGrade.NBC'+str(num), 'w') as f:
        for i in range(len(grade)):
            for j in range(len(grade[i])):
                if j > 20:
                    break
                f.write(str(i + 1))
                f.write('\t')
                f.write(str(grade[i][j][0]))
                f.write('\t')
                f.write(str(grade[i][j][1]))
                f.write('\n')
    print('save success')


def nbc(user_data, fileNum):
    # 用户行为日志导入（模拟为用户-物品-评分矩阵，0表示用户尚未评分）（数据为随机生成）
    [userID, movieID] = np.shape(user_data)
    grade = []
    for i in range(userID):              # 朴素贝叶斯-列表嵌套形式逐个遍历用户信息进行打分
        print(i)
        grade.append([])
        for j in range(movieID):
            print(j)
            if user_data[i, j] == 0:
                progress = []
                for k in range(5):
                    progress.append([])
                    for p in range(userID):
                        if user_data[p, j] == k+1:
                            progress[k].append(user_data[p, :])
                link = list()
                for k in range(5):
                    _pro_ = np.array(progress[k])
                    if not progress[k]:
                        link.append(0)
                    else:
                        _pro_ = np.array(progress[k])
                        lv = 1
                        for p in range(movieID):
                            if p != j:
                                lv = lv*(np.sum(_pro_[:, p] == user_data[i, p]) / np.shape(_pro_)[0])
                        link.append(lv)
                grade[i].append([j, link.index(max(link)) + 1])
        grade[i].sort(key=lambda x: x[1], reverse=True)
    show(grade)
    saveGrade(grade, fileNum)
