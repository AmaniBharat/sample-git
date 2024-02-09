from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
##########CREATING THE POM PAGE FOR PYTEST PYTHON FILE######
#creating the class ########
class IMDbSearchPage:
######INIALISING THE DEFAULT PARAMETER "SELF" ######
    def __init__(self, driver):
        self.driver =driver
        #USING ELEMENT LOCATORS WE ARE ACCESSING THE WEBPAGE ELEMENTS
        self.name_click =(By.XPATH, "//*[@id='nameTextAccordion']/div[1]/label/span[1]")
        self.name_text=(By.NAME, 'name-text-input')
        self.birth_click=(By.XPATH,"//*[@id='birthDateAccordion']/div[1]/label/span[1]/div")
        self.birth_startdate=(By.NAME,"birth-date-start-input")
        self.birth_enddate = (By.NAME, "birth-date-end-input")
        self. birthday_click =(By.XPATH, "//*[@id='birthdayAccordion']/div[1]/label/span[1]/div")
        self.birthday_data =(By.NAME, "birthday-input")
        self.awards_click=(By.XPATH,"//*[@id='awardsAccordion']/div[1]/label")
        self.page_topics=(By.XPATH, "//*[@id='pageTopicsAccordion']/div[1]/label")
        self.death_click=(By.XPATH,"//*[@id='deathDateAccordion']/div[1]/label/span[1]/div")
        self.death_start=(By.NAME,"death-date-start-input")
        self.death_end=(By.NAME,"death-date-end-input")
        self.gender_click=(By.XPATH,"//*[@id='genderIdentityAccordion']/div[1]/label/span[1]/div")
        self.credit_click=(By.XPATH,"//*[@id='filmographyAccordion']/div[1]/label")
        self.adult_name =(By.XPATH, '//*[@id="adultNamesAccordion"]/div[1]/label/span[1]/div')
        self.radio_button=(By.XPATH, '//*[@id="include-adult-names"]')
        self.see_click=(By.XPATH,'//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button[2]/span')
#########NAME DETAILS IN THE WEBPAGE USING FUNCTION WE ARE GIVING THE INPUT#####
    def name_details(self,name):
        self.driver.find_element(*self.name_click).click()
        self.driver.find_element(*self.name_text).send_keys(name)
#######CREATING THE BIRTH DETAILS FUNCTION TO GIVE INPUT TO THE ELEMENTS IN THE PYTEST PAGE####
    def birth_details(self,sdate,edate):
        self.driver.find_element(*self.birth_click).click()
        self.driver.find_element(*self.birth_startdate).send_keys(sdate)
        self.driver.find_element(*self.birth_enddate).send_keys(edate)
#######CREATING THE BIRTH DETAILS FUNCTION ####
    def birthday_details(self,bdate):
        self.driver.find_element(*self.birthday_click).click()
        self.driver.find_element(*self.birthday_data).send_keys(bdate)
######CREATING THE AWRADS DETAILS FUNCTION TO GIVE THE INPUT IN THE PYTEST PAGE ####
    def awards_details(self):
        self.driver.find_element(*self.awards_click).click()
#####CRETAING THE PAGE DETAILS FUNCTION#####
    def page_details(self):
        self.driver.find_element(*self.page_topics).click()
###CREATING THE DEATH DETAILS FUNCTION###
####BY USING THE SDEATH AND EDEATH AS A PARAMETRES IN THE FUNCTION WE ARE GIVING THE INPUT IN THE PYTEST PAGE###
    def death_details(self,sdeath,edeath):
        self.driver.find_element(*self.death_click).click()
        self.driver.find_element(*self.death_start).send_keys(sdeath)
        self.driver.find_element(*self.death_end).send_keys(edeath)
#####CREATING THE GENDER DETAILS FUNCTION TO SELECT THE GENDER ###
    def gender_details(self):
        self.driver.find_element(*self.gender_click).click()
######CRAETING THE CREDIT DETAILS FUNCTION IN POM PAGE####
    def credit_details(self):
        self.driver.find_element(*self.credit_click).click()
    def adult_details(self):
        self.driver.find_element(*self.adult_name).click()
        self.driver.find_element(*self.radio_button).click()
#####CREATING THE CLICK_DEATILS FUNCTION TO CLICK THE SEARCH BUTTON IN THE WEBPAGE###
    def click_details(self):
        self.driver.find_element(*self.see_click).click()





