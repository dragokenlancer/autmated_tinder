from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from secrets import email, password, phone, pickup
#only uses facebook.
class BumbleBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self):
        self.driver.get('http://bumble.com/get-started')
        sleep(2)

        fb_btn = bot.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div') 
        fb_btn.click()
        base_window = self.driver.window_handles[0] 
        self.driver.switch_to.window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)
        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(password)
        l_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        l_btn.click()
        sleep(15)#i use 2fa so have to wait for the prompt one my phone
        self.driver.switch_to.window(base_window)

    def like(self):
        like_btn = bot.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')
        like_btn.click()
    def pas(self):#named because python
        pass_btn = bot.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span')
        pass_btn.click()
    def paywall_close(self):
        close_paywall = bot.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div/div[2]/div/div[2]')
        close_paywall.click()
        #refresh the page to prevent a endless loop
        self.driver.get('http://bumble.com/get-started')
        sleep(2)
    def auto_swipe(self):
        counter = 0 
        while True:
            sleep(1)
            try:
                if counter < 9:
                    self.like()
                    counter += 1
                else:
                    self.pas()
                    counter = 0
            except Exception:
                try:
                    self.paywall_close()
                except Exception:    
                    print("error")
                    break

bot = BumbleBot()
bot.login()
bot.auto_swipe()
