from selenium import webdriver
from realtimekeyword import getNaverRealtimekeyword
import time
from bs4 import BeautifulSoup 
from posting import TistoryPostingBot
import datetime


#using chromdriver
driver = webdriver.Chrome("chromedriver.exe") 

driver.implicitly_wait(3)

driver.get("https://search.naver.com/search.naver")

keywordlist = getNaverRealtimekeyword()
#print(keywordlist)

alltext = []
#first page, search(not use)
#driver.find_element_by_id("query").send_keys("")
#driver.find_element_by_class_name("sch_smit").click()

#i use rank 1 to 10
for i in range(0,5):
    driver.find_element_by_id("nx_query").clear() #clear
    driver.find_element_by_id("nx_query").send_keys(keywordlist[i]) # next keyword
    driver.find_element_by_class_name("bt_search").click() #serach

    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')    

    title_list = soup.select("._sp_each_title")

    #print(title_list)
    for tag in title_list:                
        alltext.append(tag)    

    time.sleep(1)

text =""
for t in alltext:
    text += str(t)

print(text)
bot = TistoryPostingBot(driver,"","","")

now = time.localtime()
s = "%04d-%02d-%02d %02d시 %02d분 인터넷 이슈!" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)

if bot.login() :
    bot.writePost(s,text,True)

