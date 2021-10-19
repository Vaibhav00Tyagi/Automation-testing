# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 11:39:43 2020

@author: Vaibhav Tyagi
"""
import json
import allure
from time import sleep
from appium import webdriver
from Methods import Method

with open('data.json', encoding="utf-8") as data_file:
    values = json.loads(data_file.read())

desc_cap = {
  "deviceName": values['deviceName'],
  "platformName": values['platformName'],
  "appPackage": values['appPackage'],
  "appActivity": values['appActivity'],
  #"noReset": True,
  "automationName": values['automationName']
    }

#create driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub",desc_cap)
driver.implicitly_wait(30)

M = Method()

@allure.story('Android Automation - Vaibhav Tyagi')
@allure.feature('Test - Automation Framework in Python')

@allure.testcase('Test Login')
def test_login():
    #trys to login
    M.login(driver,values['user1']['name'],values['user1']['pass'])
    sleep(5)
    
@allure.testcase('Test raising a query in help center')
def test_query():
    #raises a query
    M.query(driver)
    sleep(5)
    
@allure.testcase('Test viewing badges and take screenshot')
def test_view_badge():
    #goes to analytics page and takes the screen shot of badges
    M.view_badge(driver)
    sleep(5)

@allure.testcase('Test Adding Product Listing')
def test_product_listing():
    #lists a product
    M.domestic_listing(driver)
    sleep(5)
    
@allure.testcase('Test switching mode between Buyer / Seller')
def test_switch():
    #switches to buyer
    M.switch(driver)
    sleep(5)
    
@allure.testcase('Test Adding a Requirement')
def test_Requirement():
    #lists a requirement
    M.imported_listing(driver)
    sleep(5)
    
@allure.testcase('Test to logout from app')
def test_logout():
    #logs out 
    M.logout(driver)
    sleep(5)
    
#logins to another account
M.login(driver,values['user2']['name'],values['user2']['pass'])
sleep(5)

'''
@allure.testcase('Test to offer to a Requirement')
def test_offer():
    #offer to a requirement
    M.offer(driver)
    sleep(5)
    
#switches as buyer
M.switch(driver)
sleep(5)

@allure.testcase('Test to bid to a Product')
def test_bid():
    #bids to a product
    M.offer(driver)
    sleep(5)
    
#logs out
M.logout(driver)
sleep(5)
#again 
M.login(driver,values['user1'][0],values['user1'][1])
sleep(5)
'''
'''
#analytics->view badges 
latest,hot and recommmended
imp parameters->thermal coal->100MT->vessekname->store listing ID->confirm these parameter
(//input[@id='ndncchk'])[0] , xpath=(//input[@id='ndncchk'])[1], xpath=(//input[@id='ndncchk'])[2]
'''








