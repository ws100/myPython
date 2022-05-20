import os
ls = os.listdir("target")
cppList = []
hList = []
for i in ls:
    if i[-4:] == ".cpp":
        cppList.append(i)
    elif i[-2:] == ".h":
        hList.append(i)
print(cppList)
print(hList)
with open("ts.md", 'w',encoding='utf-8') as s:
    s.write("# 头文件\n")
    for i in hList:
        s.write("## " + i+"\n")
        s.write("```C++\n")
        with open("target/" + i, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for lin in lines:
                s.write(lin)
        s.write("```\n")
    s.write("# 源文件\n")
    for i in cppList:
        s.write("## " + i+"\n")
        s.write("```C++"+"\n")
        with open("target/" + i, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for lin in lines:
                s.write(lin)
        s.write("```\n")
os.system("pandoc ts.md -s -o 代码.docx")
