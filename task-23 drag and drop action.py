from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
chrome_service = ChromeService(r"C:\Users\Dell\Desktop\New folder\chromedriver.exe")#launching the web browser
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")#opening the url in the web browser
time.sleep(10)
from selenium.webdriver.common.by import By
driver.switch_to.frame(0)#switching to the frame in the website
s1=driver.find_element(By.ID,"draggable")#finding the elements by using the id which is dragged stored in s1 variable
d1=driver.find_element(By.ID,"droppable")#finding the element by using the id which is to be dropped in the particular location stored in d1 variable
time.sleep(10)#wait until the number of seconds specified by using the sleep method
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)#using the action chains concept
time.sleep(10)
actions. drag_and_drop(s1,d1)#by using drag_and_drop method to perform the required action of dragging and dropping
actions. perform()#use perform method to accomplish the actions thathas to be done
time. sleep(10)

