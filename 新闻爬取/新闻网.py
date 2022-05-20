import requests
import os
from bs4 import BeautifulSoup
import pymysql

db = pymysql.connect(host="localhost", user="ws1128", password="031128", database="news")
cursor = db.cursor()

class news:
    def __init__(self, title, url, time, index):
        self.title = title
        self.url = url
        self.time = time
        self.index = index
    def save_text(self):
        path = ".\新闻"
        if not os.path.exists(path):
            os.mkdir(path)
        response = requests.get(self.url).content.decode("utf-8")
        soup = BeautifulSoup(response, "html.parser")
        content = soup.find_all("div", id="content")[0].find_all("p")
        cont = ""
        print(self.time)
        with open(path + "\\" + "{}-{}-{}.txt".format(self.index, self.time, self.title), 'w', encoding="utf-8") as file:
            for i in content:
                if i.string != None:
                    cont += i.string + "\n"
                    file.write(i.string + "\n")
        cursor.execute(f"insert into title(id,head,time,content) values({self.index},'{self.title}','{self.time}','{cont}')")
        db.commit()

index = 1
for i in range(1, 300):
    url = "https://news.chd.edu.cn/300/list{}.htm".format(i)
    response = requests.get(url).content.decode("utf-8")
    soup = BeautifulSoup(response, "html.parser")
    soupList = soup.find_all("a", class_ = "column-news-item")

    page = 1
    for j in soupList:
        if not j['href'][:4] == "http":

            url = "https://news.chd.edu.cn/"+j['href']
            title = j.find_all("span")[0].string.replace('/',' ')
            time = j.find_all("span")[1].string
            n = news(title, url, time, index)
            n.save_text()
            index = index + 1
            page = page + 1
    print("第{}页 第{}篇已爬完 共{}篇".format(i, page, index))



