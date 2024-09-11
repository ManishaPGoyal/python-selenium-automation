from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.refresh()
driver.implicitly_wait(10)
# open the url https://www.amazon.com/
driver.get('https://www.amazon.com/')

# find element search filed in amazon
#By CSS command in console $$("#twotabsearchtextbox")
driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")
#this command is same to
driver.find_element(By.ID,'twotabsearchtextbox')
# USED class attribute
# with one class value command $$(".nav-input")
driver.find_element(By.CSS_SELECTOR,".nav-input")
#with multiple class value,use . with every class  command is $$(".nav-input.nav-progressive-attribute")
driver.find_element(By.CSS_SELECTOR,".nav-input.nav-progressive-attribute")
#use can also use tag name with class attribute and command is $$("input.nav-input.nav-progressive-attribute")
driver.find_element(By.CSS_SELECTOR,"input.nav-input.nav-progressive-attribute")
# use tag name, id and one class value together command is $$("input#twotabsearchtextbox.nav-input")
driver.find_element(By.CSS_SELECTOR,"input#twotabsearchtextbox.nav-input")
#use id and multiple class value command is  $$("input#twotabsearchtextbox.nav-input.nav-progressive-attribute")
driver.find_element(By.CSS_SELECTOR,"input#twotabsearchtextbox.nav-input.nav-progressive-attribute")
#find flag-iconEN command on java script console is $$(".nav-a.nav-a-2.icp-link-style-2")
driver.find_element(By.CSS_SELECTOR,".nav-a.nav-a-2.icp-link-style-2")
#can use attribute if you dont want to use id or class command is $$("[placeholder='Search Amazon']")

#can use attribute if you dont want to use id or class and tag name ,command is $$("input[placeholder='Search Amazon']")

#can use any attribute command $$("input[aria-label='Search Amazon']") or $$("[aria-label='Search Amazon']")

#can use class and attribute both . recommend to use class before attribute and command is $$(".nav-input[aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR,".nav-input[aria-label='Search Amazon']")
# can use multiple class and attribute and command is $$(".nav-input.nav-progressive-attribute[aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR,".nav-input.nav-progressive-attribute[aria-label='Search Amazon']")
#can multiple classes and multiple attribute and command is  $$(".nav-input.nav-progressive-attribute[aria-label='Search Amazon'][aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR,".nav-input.nav-progressive-attribute[aria-label='Search Amazon'][aria-label='Search Amazon']")

# can use full value and command is $$("[href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.CSS_SELECTOR,"[href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
#can use partial value by using asterix before = sign and command is $$("[href*='notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR,"[href*='notification_condition_of_use']")
# use parent id and child attribute of privacy and command is $$("#legalTextRow [href*='privacy']") # use space between parent id and child attribute
driver.find_element(By.CSS_SELECTOR,"#legalTextRow [href*='privacy']")

#use parent class attribute, then child id then child attribute for the same privacy notice command is $$(".a-box-inner #legalTextRow [href*='privacy']") and space should be there in parent class , id and attribute
driver.find_element(By.CSS_SELECTOR,".a-box-inner #legalTextRow [href*='privacy']")

#use partial match for id and class , in that case use them as attribute command for class $$("[class*='fHanxz']") on target site
#use partial match for id comand for that $$("[id*='component-header']") on target site














