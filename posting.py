from selenium import webdriver
from realtimekeyword import getNaverRealtimekeyword
import time
from bs4 import BeautifulSoup 


class TistoryPostingBot:
    def __init__(self,driver, dir, id,password):
        self.id = id
        self.dir =dir
        self.password = password
        self.driver = driver
        return

    def login(self):
        dir = self.dir + '/manage'
        driver = self.driver
        driver.get(dir)
        
        driver.find_element_by_id("loginId").send_keys(self.id)
        driver.find_element_by_id("loginPw").send_keys(self.password)
        driver.find_element_by_class_name("btn_login").click()         
        return True

    def writePost(self, title, text ,istag =False):
        dir = self.dir + '/admin/entry/post/'
        driver = self.driver
        driver.get(dir)
        driver.find_element_by_id("titleBox").send_keys(title)

        if istag == False:
            driver.switch_to_frame(driver.find_element_by_id("tx_canvas_wysiwyg"))
            driver.find_element_by_class_name("tx-content-container").send_keys(text)
            driver.switch_to_default_content()
        else:
            driver.find_element_by_id("tx_switchertoggle").click()
            driver.find_element_by_id("tx_canvas_source").send_keys(text)


        time.sleep(2)

        #post btn
        driver.find_element_by_xpath("//*[@id=\"tistoryFoot\"]/div/button[3]").click()

        #popup close
        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        driver.find_element_by_id("btnSubmit").click()

