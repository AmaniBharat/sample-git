from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
############launching the browser by using the driver variable##################
chrome_service = ChromeService(r"C:\Users\Dell\Desktop\New folder\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
##############launching the url in the browser######
driver.get("https://www.saucedemo.com/")
##########maximising the opened url window################
driver.maximize_window()
##########error handling by using exceptions#########
wait = WebDriverWait(driver, 15, ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementNotInteractableException,
                                                     TimeoutException])
########user id details##########
user_click=wait.until(EC.presence_of_element_located((By.ID,"user-name")))
user_click.click()
user_click.send_keys("standard_user")
##########user id password#######
user_password=wait.until(EC.presence_of_element_located((By.ID,"password")))
user_password.click()
user_password.send_keys("secret_sauce")
##########clicking the login button########
login_click=wait.until(EC.presence_of_element_located((By.ID,"login-button")))
login_click.click()
time.sleep(5)



