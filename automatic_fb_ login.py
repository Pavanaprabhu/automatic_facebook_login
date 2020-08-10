 
from selenium import webdriver
browser=webdriver.Chrome('C:\\Users\Pavana Prabhu\chromedriver_win32 (1)\chromedriver.exe')
browser.get('http://www.facebook.com/')

user_id="yr@gmail.com"
password="yrfbpassword"

ep=browser.find_element_by_id("email")
ep.send_keys(user_id)

ps=browser.find_element_by_id("pass")
ps.send_keys(password)

login=browser.find_element_by_id("u_0_b")
login.click()
