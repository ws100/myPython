from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

web = Edge()
web.get("https://docs.qq.com/form/page/DYXZRVElmVU5mc1RF")
input()


for i in range(100):
    print(f"第{i}份开始")
    p = '/html/body/div[16]/div/ul/li[3]/div[2]'

    while len(web.find_elements(by=By.XPATH, value=p)) == 0:
        time.sleep(0.1)
    web.find_elements(by=By.XPATH, value=p)[0].click()
    path1 = '//*[@id="root"]/div[3]/div/div[2]/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/textarea'
    path2 = '//*[@id="root"]/div[3]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/textarea'
    path3 = '//*[@id="root"]/div[3]/div/div[2]/div[3]/div[1]/div[1]/div[3]/div/div[2]/div[2]/div/textarea'
    textArea1 = web.find_elements(by=By.XPATH, value=path1)[0]
    textArea2 = web.find_elements(by=By.XPATH, value=path2)[0]
    textArea3 = web.find_elements(by=By.XPATH, value=path3)[0]
    textArea1.send_keys("1")
    textArea2.send_keys("2")
    textArea3.send_keys("3")
    btn = '//*[@id="root"]/div[3]/div/div[2]/div[3]/div/div[1]/div[5]/button'
    enBtn = 'dui-button-container'
    enenBtn = 'form-submit-result-text-btns'
    web.find_elements(by=By.XPATH, value=btn)[0].click()
    time.sleep(0.2)
    web.find_elements(by=By.CLASS_NAME, value=enBtn)[1].click()
    time.sleep(0.2)
    web.get("https://docs.qq.com/form/page/DYXZRVElmVU5mc1RF")
    print(f"第{i}份完成")
