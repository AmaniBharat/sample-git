path1=r"C:\Users\Dell\Desktop\sample\screenshot.png"#path1 location specified
#path12=r"C:\Users\Dell\Desktop\sample\screenshot.docx"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
chrome_service = ChromeService(r"C:\Users\Dell\Desktop\New folder\chromedriver.exe")#getting the executable file of google chrome
driver = webdriver.Chrome(service=chrome_service)
from selenium.webdriver.common.by import By
import time
driver.get("https://labour.gov.in/photo-gallery")#opening the gallery page from the labour.gov.in website
#driver.find_element(By.CLASS_NAME,"open_button").click()
#driver.implicitly_wait(10)
#driver.maximize_window()
#driver.find_element(By.LINK_TEXT,"Media").click()
#time.sleep(10)
#driver.find_element(By.CLASS_NAME,"menu__link").click()
#time.sleep(10)
driver.maximize_window()#maximising the website window
driver.execute_script("window.scrollTo(0,500);")#getting to scroll the website page
driver.save_screenshot(path1)#saving the got screenshot in specified path which is mentioned in the path1 variable
time.sleep(3)#waiting in the webpage until the specified number of seconds using sleep method
print("check the screenshot of the page in path1 ")


