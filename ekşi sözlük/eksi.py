from lib2to3.pgen2 import driver
from selenium import webdriver
import random
import time

browser = webdriver.Firefox(executable_path="/home/uni/Masaüstü/selenium/ekşi sözlük/geckodriver")
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

entry=[]
pageCount=1
entryCount=1
while pageCount<=10:
    randomPage=random.randint(1,1290)
    newUrl=url+str(randomPage)
    browser.get(newUrl)
    
    content=browser.find_elements_by_css_selector(".content")
    for i in content:
        entry.append(i.text)
    time.sleep(2)
    pageCount+=1
with open("antry.txt","w",encoding="utf-8") as file:

    for a in entry:
        file.write(str(pageCount)+".\n"+a+"\n")
        file.write("-----------------------------------------------")
        pageCount+=1



browser.quit()