import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
data=pd.read_excel("case4.1.xls","case4.1",index_col=0,usecols="A,C:J",skiprows=2)
distortions=[]#簇内误差平方和  SSE
for i in range(2,10):
    Kmeans_model=KMeans(n_clusters=i)
    predict_=Kmeans_model.fit_predict(data)
    distortions.append(Kmeans_model.inertia_)
    print("簇内误差平方和：",distortions)
#SSE  手肘法
plt.plot(range(2,10),distortions,marker='x')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.title('distortions')
plt.show()