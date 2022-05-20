# 2020 人数 6224
# 2019 人数 6288
# 2018 人数 6276
import pandas as pd
import pymysql
db = pymysql.connect(user='ws1128',
                     password='031128',
                     database='stu')
cursor = db.cursor()
a = pd.read_csv("2.csv", encoding='gbk', header=None)
print(len(a))
for i in range(len(a)):
    sql = f"SELECT * from sheet1 WHERE XM = '{a.loc[i, 0]}';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) == 0:
        print("非个人或查无此人")
    elif len(result) == 1:
        print(result[0][0]//1000000)
    else:
        print(result)
    # print(f"SELECT * from sheet1 WHERE XM = '{a.loc[i, 0]}';")
