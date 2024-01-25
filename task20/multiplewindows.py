from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
chrome_service = ChromeService(r"C:\Users\Dell\Desktop\New folder\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.cowin.gov.in/")
parent=driver.current_window_handle
print("parent window is",parent)
time.sleep(4)
driver.maximize_window()
time.sleep(5)
from selenium.webdriver.common.by import By
time.sleep(5)
driver.find_element(By.LINK_TEXT,"FAQ").click()
time.sleep(5)
window1=driver.current_window_handle
print("first window handle id is",window1)
driver.find_element(By.LINK_TEXT,"PARTNERS").click()
window2=driver.current_window_handle
print("second window handle id is",window2)
time.sleep(5)
all=driver.window_handles
print(all)
for i in all:
    if i!=parent:
        driver.switch_to.window(i)
        time.sleep(5)
        driver.close()
        time.sleep(5)





