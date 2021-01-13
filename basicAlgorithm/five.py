import numpy as np


fileName = 'saveGrade.CF'
data = np.zeros((943, 1682))


if __name__ == '__main__':
    for i in range(5):
        with open('saveGrade.CF'+str(i)) as grade:
            for gra in grade:
                grad = gra[:-1].split('\t')
                data[int(grad[0]) - 1, int(grad[1]) - 1] += float(grad[2])
    data = data/5
    with open('finalGrade.txt', 'w') as final:
        for i in range(np.shape(data)[0]):
            for j in range(np.shape(data)[1]):
                final.write(str(data[i, j]))
                final.write('\t')
            final.write('\n')




