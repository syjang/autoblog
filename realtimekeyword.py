import requests
from bs4 import BeautifulSoup

def getNaverRealtimekeyword():
    html =requests.get("https://www.naver.com").text
    #print(html)
    soup = BeautifulSoup(html,'html.parser')
    title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
    #print(title_list)
    ret = []
    for idx ,title in enumerate(title_list,1):
        ret.append(title.text)

    return ret