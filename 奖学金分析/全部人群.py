import pymysql
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter

plt.rcParams['font.sans-serif'] = 'SimHei'
db = pymysql.connect(user='root',
                     password='031128',
                     database='stu3')
cursor = db.cursor()
xList = ['0.0-1.0', '1.0-2.0', '2.0-3.0', '3.0-4.0', '4.0-5.0']

with open("res2.md", 'w') as f:
    f.write("# GPA统计\n")
    f.write(f"## 全体\n")
    f.write("|      |0.0-1.0|1.0-2.0|2.0-3.0|3.0-4.0|4.0-5.0|\n")
    f.write("| ---- | ---- | ---- | ---- | ---- | ---- |\n")
    gpaList = []
    cursor.execute(f"select count(DISTINCT `学号`) from sheet1 where gpa >= 4.0  and gpa is not null")
    gpaList.append(cursor.fetchall()[0][0])
    cursor.execute(f"select count(DISTINCT `学号`) from sheet1 where gpa >= 3.0 and gpa <4.0")
    gpaList.append(cursor.fetchall()[0][0])
    cursor.execute(f"select count(DISTINCT `学号`) from sheet1 where gpa >= 2.0 and gpa <3.0")
    gpaList.append(cursor.fetchall()[0][0])
    cursor.execute(f"select count(DISTINCT `学号`) from sheet1 where gpa >= 1.0 and gpa <2.0")
    gpaList.append(cursor.fetchall()[0][0])
    cursor.execute(f"select count(DISTINCT `学号`) from sheet1 where gpa <1.0")
    gpaList.append(cursor.fetchall()[0][0])
    number = sum(gpaList) / 100
    f.write(f"| 人数 | {gpaList[4]} | {gpaList[3]} | {gpaList[2]} | {gpaList[1]} | {gpaList[0]} |\n")
    f.write("| 占比 | {:.2f}% | {:.2f}% | {:.2f}% | {:.2f}% | {:.2f}% |\n".format(gpaList[4] / number,
                                                                                    gpaList[3] / number,
                                                                                    gpaList[2] / number,
                                                                                    gpaList[1] / number,
                                                                                    gpaList[0] / number))
    gpaList.reverse()
    plt.bar(xList, gpaList)
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d 人'))
    for x, y in zip(xList, gpaList):
        plt.text(x, y, '%i人' % y, ha='center', va='bottom')
    plt.title(f"全体获奖人数GPA分布图")
    plt.xlabel('GPA', fontsize=15)
    plt.ylabel('人数', fontsize=15)
    plt.savefig(f'.res.assets/全体获奖人数GPA分布图.png', dpi=200)
    plt.show()
    f.write("\n")
    f.write(f"![全体获奖人数GPA分布图](.res.assets/全体获奖人数GPA分布图.png)\n")
    f.write('<div STYLE="page-break-after: always;"></div>\n')
    # print(i, end="-")
    print(gpaList)

