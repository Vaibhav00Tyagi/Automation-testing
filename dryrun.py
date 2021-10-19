# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 22:29:52 2021

@author: Vaibhav Tyagi
"""
import json
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
  "noReset": True,
  "automationName": values['automationName']
    }

#create driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub",desc_cap)
driver.implicitly_wait(30)

M = Method()

M.last_listing(driver)

sleep(5)

M.domestic_listing(driver)




 