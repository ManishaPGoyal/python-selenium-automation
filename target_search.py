from selenium import webdriver
from selenium.webdriver import Keys
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

driver.get("https://www.target.com/")
#sleep(20)

#Search filed =>tea
driver.find_element(By.ID,'search').send_keys('tea')
# if user press enter instead of cliclking the search icon then command is below and you need to remove click command
#driver.find_element(By.ID,'search').send_keys('tea', Keys.ENTER)
#Search button=> click
#command type on console $x("//button[@data-test='@web/Search/SearchButton']")
driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()

#when you run first time this code as target website is slow and selenium is fast so test will fail . so put sleep(6) to slow down the execution of the code
sleep(6)
#Verification  $x("//div[@data-test='resultsHeading']")
actual_result=driver.find_element(By.XPATH,"//div[@data-test='resultsHeading']").text
expected_result='tea'
# use below to make and check the test fail
#expected_result='tea1233444'
#below will print  default assert exception message if test fails
#assert expected_result in actual_result
# it will print our message when test fails
assert expected_result in actual_result,f'Expected {expected_result} but got {actual_result}'
print('Test case passed')
#it will close the browser
driver.quit()
