# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 21:28:56 2020

@author: Vaibhav Tyagi
"""
import time
from appium import webdriver

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

#switch as buyer
driver.find_element_by_id("com.coalshastralive.android.app:id/switchbutton").click()

#open requirement listing page
driver.find_element_by_id("com.coalshastralive.android.app:id/newrfqpage").click()

#selecting type of product
driver.find_element_by_id("com.coalshastralive.android.app:id/productDetailsDomesticRb").click()

#selecting coal type
driver.find_element_by_id("com.coalshastralive.android.app:id/indiancoaltype").click()

#selecting one of them
time.sleep(2)
webdriver.common.touch_action.TouchAction(driver).tap(x=320, y=860).perform()

#entering mine name
driver.find_element_by_id("com.coalshastralive.android.app:id/minename").send_keys("sfafafad")

#entering calorific value
driver.find_element_by_id("com.coalshastralive.android.app:id/editcalorificwithmine").send_keys("4624")

#entering quantity
driver.find_element_by_id("com.coalshastralive.android.app:id/qauntityvalue").send_keys("10000")

#selecting date of availability
driver.find_element_by_id("com.coalshastralive.android.app:id/dateofavailability").click()
driver.find_element_by_id("com.coalshastralive.android.app:id/ok").click()

#scrolling to bottom of the page
driver.swipe(491,1317,508,554)

#select to show price
driver.find_element_by_id("com.coalshastralive.android.app:id/yes").click()

#entering price
driver.find_element_by_id("com.coalshastralive.android.app:id/editprice").send_keys("4500")

#for minimum order Quantity
driver.find_element_by_id("com.coalshastralive.android.app:id/miniorderqauntity").click()

#selecting one of them
time.sleep(2)
webdriver.common.touch_action.TouchAction(driver).tap(x=320, y=1060).perform()

#entering No. of Lifting days
driver.find_element_by_id("com.coalshastralive.android.app:id/liftingdays").send_keys("3")

#scrolling to bottom of the page
driver.swipe(491,1317,508,554)

#submitting requirement
driver.find_element_by_id("com.coalshastralive.android.app:id/submitform").click()










