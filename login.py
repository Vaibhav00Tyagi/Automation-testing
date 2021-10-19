# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:53:26 2020

@author: Vaibhav Tyagi
"""
import time
from appium import webdriver

desc_cap = {
  "deviceName": "G9UDU17B10000562",
  "platformName": "Android",
  "appPackage": "com.coalshastralive.android.app",
  "appActivity": ".activity.Splash_Screen_Activity"
    }

#create driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub",desc_cap)
driver.implicitly_wait(30)

#open login menu 
driver.find_element_by_id("com.coalshastralive.android.app:id/loginpage").click()

#delay of five seconds
time.sleep(3)

#login into app
driver.find_element_by_id("com.coalshastralive.android.app:id/emailtv").send_keys("test1@coalshastra.com")
driver.find_element_by_id("com.coalshastralive.android.app:id/passtv").send_keys("12345678")
driver.find_element_by_id("com.coalshastralive.android.app:id/loginll").click()

#delay of five seconds
time.sleep(3)

#skip intro
webdriver.common.touch_action.TouchAction(driver).tap(x=968, y=367).perform()
webdriver.common.touch_action.TouchAction(driver).tap(x=288, y=508).perform()
webdriver.common.touch_action.TouchAction(driver).tap(x=865, y=484).perform()
webdriver.common.touch_action.TouchAction(driver).tap(x=924, y=1500).perform()
webdriver.common.touch_action.TouchAction(driver).tap(x=533, y=1818).perform()

driver.find_element_by_id("com.coalshastralive.android.app:id/switchbutton").click()
