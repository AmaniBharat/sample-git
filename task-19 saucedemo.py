from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
chrome_service = ChromeService(r"C:\Users\Dell\Desktop\New folder\chromedriver.exe")#the path of the browser exe file
driver = webdriver.Chrome(service=chrome_service)#launching the browser
driver.get("https://www.saucedemo.com/")#launching the website using driver variable
data1=driver.current_url #displaying the current Url in the chrome browser
print(data1)
data=driver.title#getting the title of current url
print(data)
print(driver.find_element(By.XPATH, "/html/body").text)#displaying the text of the current url page


