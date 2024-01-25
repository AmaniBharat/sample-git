from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
chrome_service = ChromeService(r"C:\Users\Dell\Desktop\New folder\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://labour.gov.in/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"open_button").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Documents").click()
time.sleep(5)
download=driver.find_element(By.XPATH,"//*[@id='fontSize']/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/a")
time.sleep(5)
download.click()
time.sleep(5)
a=driver.switch_to.alert
time.sleep(5)
a.accept()
time.sleep(10)
