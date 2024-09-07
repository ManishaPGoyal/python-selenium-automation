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

# open the url https://www.amazon.com/
driver.get('https://www.amazon.com/')

# Locate element use followung command
#driver.find_element(By.ID,'value') #By ID. /value

#Locate element By ID
driver.find_element(By.ID,'twotabsearchtextbox')
driver.find_element(By.ID,'nav-logo-sprites')

#Locate element by XPATH
driver.find_element(By.XPATH,"//img[@alt='Deals']")
#command on console of web page $x("//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon']")
#command on console of web page $x("//input[@name='field-keywords']")
driver.find_element(By.XPATH,"//input[@name='field-keywords']")
#command on console of webpage using one attribute $x("//a[@class='nav-a  ']")
driver.find_element(By.XPATH,"//a[@class='nav-a  ']")
#command on console of webpage for using multiple attribute $x("//a[@class='nav-a  ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.XPATH,"//a[@class='nav-a  ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
#multiple attribute $x("//a[@class='nav-a  ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers' and @tabindex='0']")
driver.find_element(By.XPATH,"//a[@class='nav-a  ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers' and @tabindex='0']")
# command to search element by text() function if text attribute is not on webpage of element $x("//a[text()='Best Sellers']")
driver.find_element(By.XPATH,"//a[text()='Best Sellers']")
#can combine the text() with other attribute $x("//a[text()='Best Sellers' and @class='nav-a  ']")
driver.find_element(By.XPATH,"//a[text()='Best Sellers' and @class='nav-a  ']")
#you can use single quotes and double quotes inside or ouside , it doesn't matter
driver.find_element(By.XPATH,'//a[text()="Best Sellers"]')
# * means any tag , it could be a,div,input  so search by attribute name , tag can be any $x("//*[text()='Best Sellers' and @class='nav-a  ']")
driver.find_element(By.XPATH,"//*[text()='Best Sellers' and @class='nav-a  ']")
driver.find_element(By.XPATH,"//*[@name='field-keywords']")
#search with parent element $x("//div[@id='nav-main']//a[text()='Best Sellers']") parent is $x("//div[@id='nav-main']") and child is "//a[text()='Best Sellers']"
driver.find_element(By.XPATH,"//div[@id='nav-main']//a[text()='Best Sellers']")
