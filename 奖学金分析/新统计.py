import pymysql
db = pymysql.connect(user='ws1128', password='031128', database='stu2')
cursor = db.cursor()
cursor.execute('SELECT year,count(id) FROM `sheet1` where status = "check" GROUP BY year;')
res1 = cursor.fetchall()
for i in res1:
    print(i)
cursor.execute('SELECT year,yearnumber,count(id) FROM `sheet1` where status = "check" GROUP BY year ,yearnumber;')
res2 = cursor.fetchall()
for i in res2:
    print(i)
