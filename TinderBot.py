from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from secrets import email, password, phone, loginwith, pickup

class Tinderbot():
    def __init__(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        login_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button') #login button
        login_btn.click()
        sleep(2)
        #login with facebook
        if loginwith == "facebook":
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button') #login with facebook
            fb_btn.click()
                #login popup windows facebook
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
            cookies_accept = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            cookies_accept.click()
            self.close_popups()#close all requests tinder asks for location/notifications/cookies
        #login with google
        elif loginwith == "google":
            g_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button') #login with google
            g_btn.click()
            sleep(10)#wait for load and or auto login with google
            base_window = self.driver.window_handles[0] 
            self.driver.switch_to.window(self.driver.window_handles[1])
            email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')#email input
            email_in.send_keys(email)
            nx_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
            nx_btn.click()
            sleep(2)
            pass_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
            pass_in.send_keys(password)
            next_btn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
            next_btn.click()
            cookies_accept = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            cookies_accept.click()
            sleep(15)#waiting for 2fa
            self.driver.switch_to.window(base_window)
            self.close_popups()#close all requests tinder asks for location/notifications/cookies
        #login with phonenumber
        elif loginwith == "phonenumber":
            ph_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[3]/button') #login with phone number
            ph_btn.click()
            sleep(2)#wait for load
            phone_n = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
            phone_n.send_keys(phone)
            cont = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
            cont.click()
            sleep(2)#wait for load
            cookies_accept = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            cookies_accept.click()
            element = WebDriverWait(bot.driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/button')))
            element.click();
            sleep(2)#wait for load
            self.close_popups()#close all requests tinder asks for location/notifications/cookies
        else:
            print("please add in the secrets.py   loginwith=   facebook,google,phonenumber")

    def close_popups(self):
        location_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]') #allow location
        location_popup.click()
        enable_notifications = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]') #enable notifications
        disable_notifications = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]') #no notfications
        disable_notifications.click() #click on of the 2 for notifications
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()
    def superlike(self):
        superlike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[3]/div/div/div/button')
        superlike_btn.click()
    def close_popup(self):
        popup4 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]') #add tinder to home screen   not interested
        popup4.click()
    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*{@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]//a') #did not get a match to test this out
        match_popup.click()
    def close_gold(self):
        gold_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        gold_btn.click()
    def close_boost(self):
        boost_bnt = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]')
        boost_bnt.click()
    def outof_boost(self):
        outof_boost = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        outof_boost.click()
    def send_match_msg(self):
        textbox = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
        textbox.send_keys(pickup[random.randint(0, len(pickup)-1)])
        send_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button')
        send_btn.click()
    def send_msg(self):
        send_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
        send_btn.click()
            
        #main loop
    def auto_swipe(self):
        counter = 0
        while True:
            sleep(0.5)
            try:
                if counter < 9:
                    self.like()
                    counter += 1
                else:
                    self.dislike()
                    counter = 0
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.send_match_msg()
                    except Exception:
                        try:
                            self.close_boost()
                        except Exception:
                            try:
                                self.close_match()
                            except Exception:
                                try:
                                    self.close_gold()
                                except Exception:
                                    try:
                                        self.outof_boost()
                                    except Exception:
                                        try:
                                            self.send_msg()
                                            break
                                        except Exception:
                                            print('-----------out of people to like----------')
                                            break

bot = Tinderbot()
bot.login()
bot.auto_swipe()