from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
chrome_service = ChromeService(r"C:\Users\Dell\Desktop\New folder\chromedriver.exe")#launching the browser
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.instagram.com/guviofficial/")#opening the website in the browser
time.sleep(10)
data=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span").text#fetching the  details of total number of followers in the website
print("the total number of followers are",data)#printing the total number of followers
time.sleep(10)
data1=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span").text#fetching the details of total number of followings in the website
print("the total number of following",data1)#printing the total number of following details
