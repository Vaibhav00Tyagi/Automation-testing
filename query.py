# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:57:09 2020

@author: Vaibhav Tyagi
"""

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

#opening the drawer
driver.find_element_by_id("com.coalshastralive.android.app:id/opendrawer").click()

#choosing help option
driver.find_element_by_id("com.coalshastralive.android.app:id/help").click()

#check for permission
try:
    driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
except:
    print("permission already given")

#writing a description
driver.find_element_by_id("com.coalshastralive.android.app:id/descrption").send_keys("testing")

#submitting the form
driver.find_element_by_id("com.coalshastralive.android.app:id/submitform").click()

#acknoledgement
driver.find_element_by_id("com.coalshastralive.android.app:id/okay").click()

#going back to home screen
driver.find_element_by_id("com.coalshastralive.android.app:id/report_screen_back").click()






