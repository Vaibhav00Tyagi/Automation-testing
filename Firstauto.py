# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:23:34 2020

@author: Vaibhav Tyagi
"""

from appium import webdriver

desc_cap = {
  "deviceName": "G9UDU17B10000562",
  "platformName": "Android",
  "appPackage": "com.coalshastralive.android.app",
  "appWaitActivity": "com.coalshastralive.android.app.OnBoardScreen.OnBoardScreen",
  "appActivity": ".activity.Splash_Screen_Activity"
    }

#create driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub",desc_cap)
driver.implicitly_wait(5)

#open as guest
driver.find_element_by_id("com.coalshastralive.android.app:id/skip").click()
