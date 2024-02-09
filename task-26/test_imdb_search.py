from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from imdb_search_page import IMDbSearchPage
import time
@pytest.fixture
######CREATING THE FUNCTION NAMED "BROWSER" AND LAUNCHING THE BROWSER USING THE DRIVER VARIABLE#####
def browser():
    chrome_service = ChromeService(r"C:\Users\Dell\Desktop\New folder\chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service)
#####MAXIMISING THE WINOOW OF THE URL PAGE####
    driver.maximize_window()
#######USING THE YIELD FUNCTION to return the driver variable value#####
    yield driver
    driver.quit()
def test_imdb_search(browser):
    imdb_search_page = IMDbSearchPage(browser)
    browser.get("https://www.imdb.com/search/name/")
    actions = ActionChains(browser)
######USING THE FOR LOOP AND ACTION CHAIN CONCEPT TO SCROLL DOWN THE PAGE TO ACCESS THE ELEMENTS#####
    for _ in range(5):
        actions.send_keys((Keys.DOWN)).perform()
    imdb_search_page.name_details("amani")
    for _ in range(30):
        actions.send_keys((Keys.DOWN)).perform()
    imdb_search_page.birth_details("29-10-2021","29-10-2080")
    for _ in range(35):
        actions.send_keys((Keys.DOWN)).perform()
    imdb_search_page.birthday_details("29-10-2021")
    for _ in range(20):
        actions.send_keys((Keys.DOWN)).perform()
####CALLING THE POM PAGE FUNCTION IN PYTEST PAGE####
    imdb_search_page.awards_details()
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys(Keys.ENTER).perform()
    for _ in range(20):
        actions.send_keys((Keys.DOWN)).perform()
    imdb_search_page.page_details()
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys(Keys.ENTER).perform()
    for _ in range(5):
       actions.send_keys(Keys.PAGE_DOWN).perform()
    imdb_search_page.death_details("12-10-2020","16-10-2020")
    for _ in range(5):
       actions.send_keys(Keys.PAGE_DOWN).perform()
    imdb_search_page.gender_details()
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys(Keys.ENTER).perform()
    for _ in range(5):
       actions.send_keys(Keys.PAGE_DOWN).perform()
    imdb_search_page.credit_details()
    for _ in range(5):
       actions.send_keys(Keys.PAGE_DOWN).perform()
    imdb_search_page.adult_details()
    for _ in range(3):
        actions.send_keys(Keys.PAGE_UP).perform()
    imdb_search_page.click_details()












