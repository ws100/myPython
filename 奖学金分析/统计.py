import os
import pandas as pd
import matplotlib.pyplot as plt
path = '2020-2021/先进集体和先进个人/附件4.长安大学2020-2021学年度本科生课程优秀奖获奖学生名单'
files = os.listdir(path)
pdList = []
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
for i in files:
    pdList.append(pd.read_excel(path+'/' + i, sheet_name=0, skiprows=1, header=0).set_index('序号'))
# print(pdList[0].iloc[:, -1])
for i in range(len(pdList)):
    print(pdList[i]['分数'].value_counts().sort_values(ascending=True).index)
    x = pdList[i]['分数'].value_counts().sort_values(ascending=True).index
    y = pdList[i]['分数'].value_counts().sort_values(ascending=True).values
    plt.pie(y, labels=x)
    plt.title(files[i])
    plt.show()
