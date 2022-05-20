import pandas as pd
import os

path = '2020-2021'
print("##" + path)
fileTempList = os.listdir(path)
fileList = []
for i in range(len(fileTempList)):
    if fileTempList[i][-4:] == '.xls' or fileTempList[i][-4:] == 'xlsx':
        if 'pass' not in fileTempList[i]:
            fileList.append(fileTempList[i])
pdList = []
for i in fileList:
    pdList.append(pd.read_excel(path +'/'+i, skiprows=1))
dicts = {}
for i in range(len(fileList)):
    # print(fileList[i])
    if '十四运' in fileList[i]:
        # print("研究生数据")
        data = pdList[i][(pdList[i]['学生类别'] == '研究生')].value_counts('年级').to_dict()
        # print(data)
        dicts[fileList[i] + "(研究生)"] = data
        # print("本科生数据")
        data = pdList[i][(pdList[i]['学生类别'] == '本科生')].value_counts('年级').to_dict()
        # print(data)
        dicts[fileList[i] + "(本科生)"] = data
    else:
        data = pdList[i].value_counts('年级').to_dict()
        # print(data)
        dicts[fileList[i]] = data
cleanDicts = {}
for i in dicts:
    # print(i)
    # print(dicts[i])
    tempDict = {}
    for j in dicts[i]:
        if '2016' in str(j):
            tempDict[2016] = dicts[i][j]
        if '2017' in str(j):
            tempDict[2017] = dicts[i][j]
        if '2018' in str(j):
            tempDict[2018] = dicts[i][j]
        if '2019' in str(j):
            tempDict[2019] = dicts[i][j]
        if '2020' in str(j):
            tempDict[2020] = dicts[i][j]
        if '2021' in str(j):
            tempDict[2021] = dicts[i][j]
    cleanDicts[i] = tempDict
for i in cleanDicts:
    print('###' + i)
    #print(cleanDicts[i])
    sum = 0
    print("|年级|比例|")
    print("| ---- | ---- |")
    for j in cleanDicts[i]:
        sum += cleanDicts[i][j]
    for j in cleanDicts[i]:
        # print("年级{}级 占比{:.2%}".format(j, cleanDicts[i][j]/sum))
        print("|{}|{:.2%}|".format(j, cleanDicts[i][j]/sum))
