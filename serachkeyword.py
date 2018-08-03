from selenium import webdriver
from realtimekeyword import getNaverRealtimekeyword
import time
from bs4 import BeautifulSoup 
from collections import OrderedDict



driver = webdriver.Chrome("chromedriver.exe")

driver.implicitly_wait(3)

driver.get("https://www.naver.com")

keywordlist = getNaverRealtimekeyword()
#print(keywordlist)


#first page, search
driver.find_element_by_id("query").send_keys(keywordlist[0])
driver.find_element_by_class_name("sch_smit").click()

#wait
time.sleep(5)
post_dict = OrderedDict()

#i use rank 1 to 10
for i in range(10):
    driver.find_element_by_id("nx_query").clear() #clear
    driver.find_element_by_id("nx_query").send_keys(keywordlist[i]) # next keyword
    driver.find_element_by_class_name("bt_search").click() #serach

    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')    

    title_list = soup.select("._sp_each_title")

    #print(title_list)

    for tag in title_list:
        if tag['href'] in post_dict:
            #return post_dict#여기 오게되면 count는 종료됩니다.            
            print(tag.text, tag['href'])
            post_dict[tag['href']] = tag.text

    time.sleep(10)
    
