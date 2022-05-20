import matplotlib
import requests
import json
# from bs4 import BeautifulSoup
from tkinter import *
from matplotlib import pyplot as plt

def dataParseMon(_data):
    return _data[0: _data.find('.')]


def dataParseDay(_data):
    return _data[_data.find('.')+1: len(_data)]


font = {'family' : 'MicroSoft YaHei',
              'weight' : 'light',
              'size'   : '20'}
matplotlib.rc("font",**font)



url = 'https://voice.baidu.com/newpneumonia/getv2?from=mola-virus&stage=publish&target=trend&isCaseIn=1&area=%E9%99%95%E8%A5%BF&callback=jsonp_1640143419877_85355'
response = requests.get(url).content.decode('utf-8')
begin = response.find('(') + 1
end = len(response) - 2
result = eval(response[begin:end])
city = result['data'][0]['name']
trend = result['data'][0]['trend']
lists = trend['list']
data = trend['updateDate']
dig = lists[0]['data']
rec = lists[1]['data']
death = lists[2]['data']
newDig = lists[3]['data']
newLoc = lists[4]['data']
print('日期 ' + str(data))
print('累计确诊 ' + str(dig))
print('治愈 ' + str(rec))
print('死亡 ' + str(death))
print('新增 ' + str(newDig))
print('新增本土' + str(newLoc))
with open('data.csv', 'w') as f:
    f.write('日期,累计确诊,治愈,死亡,新增,新增本土\n')
    for i in range(0, len(data)):
        f.write('%s月%s日,%d,%d,%d,%d,%d\n' % (dataParseMon(data[i]), dataParseDay(data[i]), dig[i], rec[i], death[i], newDig[i], newLoc[i]))
    f.close()
plt.figure(figsize=(16, 10))
plt.plot(data, dig,label = "累计确诊",color = "orange")
plt.plot(data, rec,label = "累计治愈",color = "green")
plt.plot(data, death,label = "死亡",color = "black")
datapar = ['{}月{}日'.format(dataParseMon(data[i]), dataParseDay(data[i])) for i in range(len(data))]
plt.xticks(data[::10],datapar[::10])
plt.title("西安疫情确诊人数")
plt.legend()
plt.grid()
plt.show()


