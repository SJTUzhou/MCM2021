# encoding=utf-8

'''
1、从本地读取判断矩阵 修改main函数中的绝对路径："ahpinput.txt"
2、对判断矩阵进行规一标准化、规一化处理
3、计算判断矩阵的最大特征根
   算法：
        a、判断矩阵*权向量得到矩阵M
        b、对M的每一个元素除以n*权向量
4. 本样例在Python3.6下运行成功，并需要安装numpy包
请保证输入的txt中的数据为正确分割的单个方阵：每行表示矩阵中一行，行内以“,"分隔不同的数据，详见一同下发的ahpinput.txt
仅支持单个矩阵操作，矩阵大小自动判断。
'''

from __future__ import division
from numpy import *
from fractions import Fraction

#读取文件，构造判断矩阵
def judgexMatrix(filePath):
    fr = open(filePath)
    data = fr.readlines()
    column = len(data[0].strip().split(','))
    row = len(data)
    print("column:", column)
    print("row:", row)
    index = 0
    judgeMatrix = zeros((row,column))
    for line in data:
        item = line.strip().split(',')
        newList = []
        for i in range(len(item)):
            value = Fraction(item[i])+0.0
            newList.append(value)
        judgeMatrix[index,:] = newList[0:column]
        index += 1
    return judgeMatrix

#对判断矩阵进行开根和归一化
def weightValue(judgematrix):
    weight = []
    standWeight = []
    sum = 0
    for item in judgematrix:
        product = 1
        for i in item:
            product *= i
        sum += (product ** (1/len(item)))
        weight.append(product ** (1/len(item)))

    for item in weight:
        standWeight.append(round(item/sum,4))
    return standWeight

def matrixMul(judgematrix,weightValue):
    res = [[0]*size(weightValue[0]) for i in range(0,len(judgematrix))]
    for i in range(len(judgematrix)):
        for j in range(size(weightValue[0])):
            for k in range(size(weightValue)):
                res[i][j] += judgematrix[i][k] * weightValue[k][j]
    return res

def trans(weightValuse):
    a = [[] for i in weightValue]
    for i in range(0,len(weightValue)):
        a[i].append(weightValue[i])
    return a

def maxRoot(judgematrix,weightValue):
    transWeightValue = trans(weightValue)
    matMul = matrixMul(judgematrix,transWeightValue)
    sum = 0
    n = len(judgematrix)
    for i in range(len(judgematrix)):
        sum += matMul[i][0]/(transWeightValue[i][0] * n)
    return sum


def consistentCheck(judgematrix,weightValue,featureNum):
    status = 'fail'
    root = maxRoot(judgematrix,weightValue)
    RI = [0.00,0.00,0.58,0.90,1.12,1.24,1.32,1.41,1.45,1.45,1.49,1.51,1.48,1.56,1.57,1.58]
    CI = round((root - featureNum)/(featureNum-1),5)
    CR = round(CI/RI[featureNum-1],4)
    if CR < 0.1:
        status =   'successful consistent check, CI=%s,'%CI+' CR=%s'%CR
    else:
        status =  'unsuccessful consisten check, CI=%s,'%CI+' CR=%s'%CR
    return status
if __name__ == "__main__":
    filePath = "ahpinput.txt"
    judgematrix = judgexMatrix(filePath)
    weightValue = weightValue(judgematrix)
    print ('weightValue is : %s' % weightValue)
    print (consistentCheck(judgematrix,weightValue,judgematrix.shape[1]))