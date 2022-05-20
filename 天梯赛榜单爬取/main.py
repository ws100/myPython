import requests
import json
import pymysql
db = pymysql.connect(host="localhost", user="ws1128", password="031128", database="trank")
cursor = db.cursor()
for j in range(2, 144):
    url = f"https://gplt.patest.cn/api/board/student_rank?page={j}&limit=100&timestamp=1650706378864"
    resp = requests.get(url).content
    rankDict = json.loads(resp)
    TempList = rankDict['data']['data']['students']
    for i in TempList:
        cursor.execute(f"insert into ranklist1(name,teamName,score) values('{i['name']}','{i['origin']}',{i['tScoreStrict']})")
        db.commit()
        #print(f"{i['name']} {i['origin']} {i['tScoreStrict']}")
    print(f"{j}页")
