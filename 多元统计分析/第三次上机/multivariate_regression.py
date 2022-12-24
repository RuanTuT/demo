import numpy as np
import pandas as pd
import statsmodels.api as sm
file = r'ex2.5.xls'
data = pd.read_excel(file,usecols="B:H")
data.columns = ['y', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6']
x = sm.add_constant(data.iloc[:,1:]) #生成自变量
y = data['y'] #生成因变量
model = sm.OLS(y, x) #生成模型
result = model.fit() #模型拟合
print(result.summary())#模型描述


def looper(limit):
    cols = ['x1', 'x2', 'x4', 'x5', 'x6']
    for i in range(len(cols)):
        data1 = data[cols]
        x = sm.add_constant(data1)  # 生成自变量
        y = data['y']  # 生成因变量
        model = sm.OLS(y, x)  # 生成模型
        result = model.fit()  # 模型拟合
        pvalues = result.pvalues  # 得到结果中所有P值
        pvalues.drop('const', inplace=True)  # 把const取得
        pmax = max(pvalues)  # 选出最大的P值
        if pmax > limit:
            ind = pvalues.idxmax()  # 找出最大P值的index
            cols.remove(ind)  # 把这个index从cols中删除
        else:
            return result


result = looper(0.05)
print(result.summary())