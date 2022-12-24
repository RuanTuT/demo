from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
iris = datasets.load_iris()
data=pd.DataFrame(np.concatenate((iris.data,np.repeat(iris.target_names,50).reshape(150,1)),axis=1),columns=np.append(iris.feature_names,'target'))
df=data.apply(pd.to_numeric,errors='ignore')

Iris1 = df.values[0:50, 0:4]
Iris2 = df.values[50:100, 0:4]
Iris3 = df.values[100:150, 0:4]
m1 = np.mean(Iris1, axis=0)
m2 = np.mean(Iris2, axis=0)
m3 = np.mean(Iris3, axis=0)
s1 = np.zeros((4, 4))
s2 = np.zeros((4, 4))
s3 = np.zeros((4, 4))
for i in range(0, 30, 1):
    a = Iris1[i, :] - m1
    a = np.array([a])
    b = a.T
    s1 = s1 + np.dot(b, a)
for i in range(0, 30, 1):
    c = Iris2[i, :] - m2
    c = np.array([c])
    d = c.T
    s2 = s2 + np.dot(d, c)
    # s2=s2+np.dot((Iris2[i,:]-m2).T,(Iris2[i,:]-m2))
for i in range(0, 30, 1):
    a = Iris3[i, :] - m3
    a = np.array([a])
    b = a.T
    s3 = s3 + np.dot(b, a)
sw12 = s1 + s2
sw13 = s1 + s3
sw23 = s2 + s3
# 投影方向
a = np.array([m1 - m2])
sw12 = np.array(sw12, dtype='float')
sw13 = np.array(sw13, dtype='float')
sw23 = np.array(sw23, dtype='float')
# 判别函数以及T
# 需要先将m1-m2转化成矩阵才能进行求其转置矩阵
a = m1 - m2
a = np.array([a])
a = a.T
b = m1 - m3
b = np.array([b])
b = b.T
c = m2 - m3
c = np.array([c])
c = c.T
w12 = (np.dot(np.linalg.inv(sw12), a)).T
w13 = (np.dot(np.linalg.inv(sw13), b)).T
w23 = (np.dot(np.linalg.inv(sw23), c)).T
# print(m1+m2) #1x4维度  invsw12 4x4维度  m1-m2 4x1维度
T12 = -0.5 * (np.dot(np.dot((m1 + m2), np.linalg.inv(sw12)), a))
T13 = -0.5 * (np.dot(np.dot((m1 + m3), np.linalg.inv(sw13)), b))
T23 = -0.5 * (np.dot(np.dot((m2 + m3), np.linalg.inv(sw23)), c))
kind1 = 0
kind2 = 0
kind3 = 0
newiris1 = []
newiris2 = []
newiris3 = []
for i in range(30, 50):
    x = Iris1[i, :]
    x = np.array([x])
    g12 = np.dot(w12, x.T) + T12
    g13 = np.dot(w13, x.T) + T13
    g23 = np.dot(w23, x.T) + T23
    if g12 > 0 and g13 > 0:
        newiris1.extend(x)
        kind1 = kind1 + 1
    elif g12 < 0 and g23 > 0:
        newiris2.extend(x)
    elif g13 < 0 and g23 < 0:
        newiris3.extend(x)
# print(newiris1)
for i in range(30, 50):
    x = Iris2[i, :]
    x = np.array([x])
    g12 = np.dot(w12, x.T) + T12
    g13 = np.dot(w13, x.T) + T13
    g23 = np.dot(w23, x.T) + T23
    if g12 > 0 and g13 > 0:
        newiris1.extend(x)
    elif g12 < 0 and g23 > 0:

        newiris2.extend(x)
        kind2 = kind2 + 1
    elif g13 < 0 and g23 < 0:
        newiris3.extend(x)
for i in range(30, 50):
    x = Iris3[i, :]
    x = np.array([x])
    g12 = np.dot(w12, x.T) + T12
    g13 = np.dot(w13, x.T) + T13
    g23 = np.dot(w23, x.T) + T23
    if g12 > 0 and g13 > 0:
        newiris1.extend(x)
    elif g12 < 0 and g23 > 0:
        newiris2.extend(x)
    elif g13 < 0 and g23 < 0:
        newiris3.extend(x)
        kind3 = kind3 + 1
correct = (kind1 + kind2 + kind3) / 60
print("样本类内离散度矩阵S1：", s1, '\n')
print("样本类内离散度矩阵S2：", s2, '\n')
print("样本类内离散度矩阵S3：", s3, '\n')
print('-----------------------------------------------------------------------------------------------')
print("总体类内离散度矩阵Sw12：", sw12, '\n')
print("总体类内离散度矩阵Sw13：", sw13, '\n')
print("总体类内离散度矩阵Sw23：", sw23, '\n')
print('-----------------------------------------------------------------------------------------------')
print('判断出来的综合正确率：', correct * 100, '%')