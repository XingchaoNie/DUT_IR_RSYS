from basicAlgorithm.dataReset import u1Test, u2Test, u3Test, u4Test, u5Test
from basicAlgorithm.CF import cf
from basicAlgorithm.NBC import nbc


def main():
    Data = [u1Test(), u2Test(), u3Test(), u4Test(), u5Test()]
    for i in range(len(Data)):
        cf(Data[i], i)
        input()
        print('doneFile!')
    """for i in range(len(Data)):
        nbc(Data[i], i)
        print('done file!')"""


if __name__ == '__main__':
    main()

