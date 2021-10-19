# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:42:25 2020

@author: Vaibhav Tyagi
"""
from appium import webdriver
import time

desc_cap = {
  "deviceName": "G9UDU17B10000562",
  "platformName": "Android",
  "appPackage": "com.coalshastralive.android.app",
  "appActivity": ".activity.Splash_Screen_Activity",
  "noReset": True
    }

#create driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub",desc_cap)
driver.implicitly_wait(30)

#click on add product listing
driver.find_element_by_id("com.coalshastralive.android.app:id/newrfqpage").click()

#using old product listing                         
driver.find_element_by_id("com.coalshastralive.android.app:id/lastrfqspinner").click()

#selecting one of them
time.sleep(2)
webdriver.common.touch_action.TouchAction(driver).tap(x=320, y=660).perform()

#selecting date of availability
driver.find_element_by_id("com.coalshastralive.android.app:id/dateofavailability").click()
driver.find_element_by_id("com.coalshastralive.android.app:id/ok").click()

#entering quantity to be displayed
driver.find_element_by_id("com.coalshastralive.android.app:id/diplayqauntity").send_keys("5000")
actions = webdriver.common.touch_action.TouchAction(driver)
actions.press(x=1000, y=1000).move_to(x=508, y=1000).release().perform()

#scrolling to bottom of the page
driver.swipe(491,1317,508,554)
driver.swipe(491,1317,508,554)

#submitting our product listing
driver.find_element_by_id("com.coalshastralive.android.app:id/submitform").click()


