# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 11:18:31 2020

@author: Vaibhav Tyagi
"""
import json
from appium import webdriver
from Locators import Locator
from time import sleep,strftime

class Method:
    def __init__(self):
        with open('data.json', encoding="utf-8") as data_file:
            self.values = json.loads(data_file.read())
    
    def guest(self,driver):
        driver.find_element_by_id(Locator.cont_guest).click()
        sleep(5)
        driver.find_element_by_id(Locator.ini_perm).click()
    
    def login(self,driver,user,passw):
        try:
            driver.find_element_by_id(Locator.login).click()
        except:
            driver.find_element_by_id(Locator.login2).click()
        sleep(5)
        driver.find_element_by_id(Locator.email).send_keys(user)
        driver.find_element_by_id(Locator.password).send_keys(passw)
        driver.find_element_by_id(Locator.submit_login).click()
        sleep(5)
        try:
            driver.find_element_by_id(Locator.ini_perm).click()
        except:
            print("already given permission for storage")
        sleep(5)
        #skip intro
        webdriver.common.touch_action.TouchAction(driver).tap(x=560, y=370).perform()
        
    def logout(self,driver):
        driver.find_element_by_id(Locator.menu).click()
        driver.find_element_by_id(Locator.profile).click()
        sleep(5)
        try:
            driver.find_element_by_id(Locator.lgout).click()
        except:
            print("Couldn't press logout")
            try:
                driver.find_element_by_xpath("//android.widget.TextView[@text='Logout']").click()
            except:
                driver.find_element_by_xpath("//android.widget.TextView[@bounds='[215,1547][970,1698]']").click()
        driver.find_element_by_id(Locator.log_yes).click()
        driver.find_element_by_id(Locator.log_back).click()
        
    def switch(self,driver):
        driver.find_element_by_id(Locator.switch).click()
        
    def last_listing(self,driver):
        driver.find_element_by_id(Locator.Add).click()
        driver.find_element_by_id(Locator.old).click()
        driver.find_element_by_xpath("//android.widget.TextView[@bounds='[91,591][893,682]']").click()
        driver.swipe(491,1317,508,554)
        driver.swipe(491,1317,508,554)
        driver.find_element_by_id(Locator.submit_prod).click()
        
    def domestic_listing(self,driver):
        try:
            driver.find_element_by_id(Locator.Add).click()
            sleep(3)
            driver.find_element_by_id(Locator.domestic).click()
            sleep(10)
            driver.find_element_by_id(Locator.coal_type).click()
            sleep(3)
            driver.find_element_by_xpath("//android.widget.TextView[@text='Thermal Coal']").click()
            driver.find_element_by_id(Locator.mining_comp).click()
            sleep(3)
            driver.find_element_by_xpath("//android.widget.TextView[@text='Eastern Coalfields Ltd.(ECL)']").click()
            driver.find_element_by_id(Locator.mine_name).send_keys(self.values['mine_name'])
            driver.find_element_by_id(Locator.cal_value).send_keys(self.values['cal_value'])
            driver.swipe(491,1317,508,554)
            driver.find_element_by_id(Locator.quantity).send_keys(self.values['quantity'])
            driver.find_element_by_id(Locator.availability).click()
            driver.find_element_by_id(Locator.ok).click()
            driver.find_element_by_id(Locator.dis_quantity).send_keys(self.values['dis_quantity'])
            driver.swipe(491,1317,508,554)
            driver.swipe(491,1317,508,554)
            driver.find_element_by_id(Locator.address).click()
            driver.find_element_by_id(Locator.sp_comm).send_keys(self.values['comment'])
            driver.find_element_by_id(Locator.submit_prod).click()
        except:
            driver.find_element_by_id(Locator.prod_back).click()

    def imported_listing(self,driver):
        try:
            driver.find_element_by_id(Locator.Add).click()
            sleep(3)
            driver.find_element_by_id(Locator.imported).click()
            sleep(10)
            driver.find_element_by_id(Locator.vessel).send_keys(self.values['vessel'])
            driver.find_element_by_xpath("//android.widget.TextView[@test='ocean phoenix']").click()
            sleep(3)
            driver.swipe(491,1317,508,554)
            driver.find_element_by_id(Locator.quantity).send_keys(self.values['quantity'])
            driver.find_element_by_id(Locator.availability).click()
            driver.find_element_by_id(Locator.ok).click()
            driver.swipe(491,1317,508,554)
            driver.swipe(491,1317,508,554)
            sleep(3)
            driver.find_element_by_id(Locator.address).click()
            driver.find_element_by_id(Locator.sp_comm).send_keys(self.values['comment'])
            driver.swipe(491,1317,508,554)
            sleep(3)
            driver.find_element_by_id(Locator.submit_prod).click()
        except:
            driver.find_element_by_id(Locator.prod_back).click()
        
    def query(self,driver):
        driver.find_element_by_id(Locator.menu).click()
        driver.find_element_by_id(Locator.helpcentre).click()
        driver.find_element_by_id(Locator.query_type).click()
        webdriver.common.touch_action.TouchAction(driver).tap(x=320, y=600).perform()
        driver.find_element_by_id(Locator.description).send_keys(self.values['comment'])
        driver.find_element_by_id(Locator.submit_issue).click()
        driver.find_element_by_id(Locator.help_ok).click()
        driver.find_element_by_id(Locator.call_back).click()
        driver.find_element_by_id(Locator.help_ok).click()
        driver.find_element_by_id(Locator.query_back).click()
        
    def offer(self,driver):
        #price = driver.find_element_by_xpath("//android.widget.TextView[@bounds='']").get_attribute("text)
        driver.find_element_by_id(Locator.req).click()
        sleep(5)
        driver.find_element_by_id(Locator.offer).click()
        driver.find_element_by_id(Locator.offer_value).send_keys(self.values['offer_value'])
        driver.find_element_by_id(Locator.offer_quantity).send_keys(self.values['offer_quantity'])
        driver.find_element_by_id(Locator.offer_lifting).send_keys(self.values['offer_lifting'])
        driver.find_element_by_id(Locator.factory).click()
        driver.swipe(491,1317,508,554)
        driver.find_element_by_id(Locator.send_offer).click()
        driver.find_element_by_id(Locator.chat_back).click()
        
    def expire_product(self,driver):
        driver.find_element_by_id(Locator.product).click()
        sleep(5)
        driver.find_element_by_id(Locator.expire).click()
        driver.find_element_by_id(Locator.prod_yes).click()
        driver.find_element_by_id(Locator.mreq_back).click()
        
    def accept_offer(self,driver):
        driver.find_element_by_id(Locator.product).click()
        sleep(5)
        driver.find_element_by_id(Locator.mreq_chat).click()
        
    def view_badge(self,driver):
        driver.find_element_by_id(Locator.stats).click()
        driver.swipe(491,1317,508,554)
        driver.swipe(491,1317,508,554)
        driver.swipe(491,1317,508,554)
        driver.find_element_by_id(Locator.view_badges).click()
        ts = strftime("%y_%m_%d_%H%M%S")
        act_name = driver.current_activity
        filename = act_name+ts
        sleep(5)
        driver.save_screenshot("c:/temp/"+filename+".png")
        driver.find_element_by_id(Locator.badges_back).click()
        driver.find_element_by_id(Locator.home).click()
        
        