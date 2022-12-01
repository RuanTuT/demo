import numpy as np
import pandas as pd
import statsmodels.api as sm
import scipy.stats as st
import matplotlib.pyplot as plt

data=pd.read_excel('eg6.1.xls', usecols='A:F')
x1=np.array(data['x1'])
x2=np.array(data['x2'])
x3=np.array(data['x3'])
x4=np.array(data['x4'])
x5=np.array(data['x5'])
x6=np.array(data['x6'])
X = pd.DataFrame(np.array((x1,x2,x3,x4,x5,x6)).T,columns=['x1','x2','x3','x4','x5','x6'])

###样本数据的协方差矩阵,
#注意np.cov默认是无偏估计，即=np.cov(X.T,ddof=1)
S = np.cov(X.T)
###样本输的相关系数矩阵
rho = np.corrcoef(X.T)
###求相关系数矩阵的特征值及其特征向量
eig,eigv = np.linalg.eigh(rho)
print(eig)###特征值
print(eigv)###特征向量
'''
主成分分析结果:
(1) 主成分标准差
(2) 主成分贡献率(方差比例)
(3) 主成分累积贡献率(方差累积比例)
(4) 主成分载荷
'''
print('各主成分的重要性：')
print('           Comp.1             Comp.2             Comp.3            Comp.4            Comp.5            Comp.6')
eig1=eig[::-1]
eigv1=eigv[:,::-1]
com_std=eig1**0.5
com_prop=eig1/np.sum(eig1)
com_cumprop=np.cumsum(eig1)/np.sum(eig1)
print('标准差      %0.8f         %0.8f         %0.8f       %0.8f       %0.8f       %0.8f'
      %(com_std[0],com_std[1],com_std[2],com_std[3],com_std[4],com_std[5]))
print('贡献率      %0.8f         %0.8f         %0.8f       %0.8f       %0.8f       %0.8f'
      %(com_prop[0],com_prop[1],com_prop[2],com_prop[3],com_prop[4],com_prop[5]))
print('累积贡献率      %0.8f         %0.8f         %0.8f       %0.8f       %0.8f       %0.8f'
      %(com_cumprop[0],com_cumprop[1],com_cumprop[2],com_cumprop[3],com_cumprop[4],com_cumprop[5]))
print('\n载荷：')

print('      Comp.1        Comp.2         Comp.3       Comp.4     Comp.5      Comp.6')

print('X1      %0.3f        %0.3f         %0.3f      %0.3f      %0.3f      %0.3f'%
      (eigv1[0,0],eigv1[0,1],eigv1[0,2],eigv1[0,3],eigv1[0,4],eigv1[0,5]))
print('X2      %0.3f        %0.3f         %0.3f      %0.3f      %0.3f      %0.3f'%
      (eigv1[1,0],eigv1[1,1],eigv1[1,2],eigv1[1,3],eigv1[1,4],eigv1[1,5]))
print('X3      %0.3f        %0.3f         %0.3f      %0.3f      %0.3f      %0.3f'%
      (eigv1[2,0],eigv1[2,1],eigv1[2,2],eigv1[2,3],eigv1[2,4],eigv1[2,5]))
print('X4      %0.3f        %0.3f         %0.3f      %0.3f      %0.3f      %0.3f'%
      (eigv1[3,0],eigv1[3,1],eigv1[3,2],eigv1[3,3],eigv1[3,4],eigv1[3,5]))
print('X5      %0.3f        %0.3f         %0.3f      %0.3f      %0.3f      %0.3f'%
      (eigv1[4,0],eigv1[4,1],eigv1[4,2],eigv1[4,3],eigv1[4,4],eigv1[4,5]))
print('X6      %0.3f        %0.3f         %0.3f      %0.3f      %0.3f      %0.3f'%
      (eigv1[5,0],eigv1[5,1],eigv1[5,2],eigv1[5,3],eigv1[5,4],eigv1[5,5]))
'''
使用statsmodels的PCA类进行主成分分析，结果与上面一致。
'''
pc = sm.PCA(X,method='eig')
print('\ncoeff------\n',pc.coeff)
print('\neigenvals------\n',pc.eigenvals)
print('\neigenvecs------\n',pc.eigenvecs)
print('\nloadings------\n',pc.loadings)


###碎石图
plt.scatter(range(len(eig1)),eig1,c='red')
plt.plot(range(len(eig1)),eig1)
plt.xlabel('主成分',size=14)
plt.ylabel('方差',size=14)
plt.title('碎石图',size=14)
plt.show()

'''
主成分值
'''
X_std=(X-np.mean(X,axis=0))/np.std(X,axis=0)
princs = X_std@pc.loadings
princs.columns=(['主成分1','主成分2','主成分3','主成分4','主成分5','主成分6'])
print(princs)
