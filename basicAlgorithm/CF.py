# 基于物品的协同过滤推荐算法实现
import numpy as np


def show(grade):
    print('*' * 5 + "基于物品的协同过滤推荐算法展示前四位用户推荐结果前两甲及评分" + '*' * 5)
    for i in range(len(grade)):
        print('*'*5 + "第{:d}位用户".format(i + 1) + '*'*5)
        for j in range(len(grade[i])):
            if j > 20:
                break
            print("电影编号:{:d}".format(int(grade[i][j][0])))
            print("推荐评分:{:.4f}".format(grade[i][j][1]))


def saveGrade(grade, num):
    with open('saveGrade.CF'+str(num), 'w') as f:
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


def cf(user_data, fileNum):
    [r, c] = np.shape(user_data)
    # 基于物品协同过滤-生成物品相似度矩阵(修正后余弦相似度计算)
    v_s = np.zeros([c, c])
    x_i = []
    x_j = []
    x_average = []
    for i in range(c):
        for j in range(c):
            if i <= j:
                v_s[i, j] = 1
            else:
                for k in range(r):
                    if user_data[k, i] != 0 and user_data[k, j] != 0:
                        x_i.append(user_data[k, i])
                        x_j.append(user_data[k, j])
                        x_average.append(np.sum(user_data[k, :])/np.sum(user_data[k, :] != 0))
                x_x_average = np.array(x_average)
                x_x_i = np.array(x_i)-x_x_average
                x_x_j = np.array(x_j)-x_x_average
                mv = ((sum(x_x_i ** 2) ** 0.5) * (sum(x_x_j ** 2) ** 0.5))
                if mv:
                    v_s[i, j] = np.sum(x_x_i * x_x_j) / ((sum(x_x_i ** 2) ** 0.5) * (sum(x_x_j ** 2) ** 0.5))
                else:
                    v_s[i, j] = 0
                v_s[j, i] = v_s[i, j]
            x_j.clear()
            x_i.clear()
            x_average.clear()
    print(v_s)
    print(user_data)
    # 基于物品协同过滤-用户未评分物品的预测评分
    grade = []
    print("done")
    for i in range(r):
        print(i)
        grade.append([])
        for j in range(c):
            if user_data[i, j] == 0:
                z_sum = 0
                m_sum = 0
                for k in range(c):
                    if user_data[i, k] != 0:
                        z_sum = z_sum + (v_s[j, k] * user_data[i, k])
                        m_sum = m_sum + v_s[j, k]
                if m_sum != 0:
                    p_u_j = z_sum/m_sum
                else:
                    p_u_j = 0
                grade[i].append([j, p_u_j])
        grade[i].sort(key=lambda x: x[1], reverse=True)
    show(grade)
    saveGrade(grade, fileNum)