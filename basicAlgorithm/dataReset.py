import numpy as np


def u1Test():
    reData = np.zeros((943, 1682))
    with open(r'E:\Python_space\ml-100k\u1.test') as data:
        for line in data:
            line = line[:-1].split('\t')
            for x in range(len(line)):
                line[x] = eval(line[x])
            reData[int(line[0]) - 1, int(line[1]) - 1] = line[2]
    return reData


def u2Test():
    reData = np.zeros((943, 1682))
    with open(r'E:\Python_space\ml-100k\u2.test') as data:
        for line in data:
            line = line[:-1].split('\t')
            for x in range(len(line)):
                line[x] = eval(line[x])
            reData[int(line[0]) - 1, int(line[1]) - 1] = line[2]
    return reData


def u3Test():
    reData = np.zeros((943, 1682))
    with open(r'E:\Python_space\ml-100k\u3.test') as data:
        for line in data:
            line = line[:-1].split('\t')
            for x in range(len(line)):
                line[x] = eval(line[x])
            reData[int(line[0]) - 1, int(line[1]) - 1] = line[2]
    return reData


def u4Test():
    reData = np.zeros((943, 1682))
    with open(r'E:\Python_space\ml-100k\u4.test') as data:
        for line in data:
            line = line[:-1].split('\t')
            for x in range(len(line)):
                line[x] = eval(line[x])
            reData[int(line[0]) - 1, int(line[1]) - 1] = line[2]
    return reData


def u5Test():
    reData = np.zeros((943, 1682))
    with open(r'E:\Python_space\ml-100k\u5.test') as data:
        for line in data:
            line = line[:-1].split('\t')
            for x in range(len(line)):
                line[x] = eval(line[x])
            reData[int(line[0]) - 1, int(line[1]) - 1] = line[2]
    return reData
