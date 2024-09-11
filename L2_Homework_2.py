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
#mentioned in instructor code below command
driver.implicitly_wait(5)
#get url
driver.get("https://www.target.com/")

sleep(15)
# click sign in button  and check it in console $x("//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']")
driver.find_element(By.XPATH,"//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
#used sleep to check click working
sleep(5)

#click sign in from side navigation and check it in console $x("//a[@data-test='accountNav-signIn']")
driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn']").click()
sleep(5)

# verify sign in page opened
# Sign in your account text is shown and command for text $x("//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']")
actual_result=driver.find_element(By.XPATH,"//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']").text
print(actual_result)
expected_result='Sign into your Target account'
assert actual_result == expected_result, f"Expected: {expected_result}, Actual: {actual_result}"
print('test case passed')

#Signin button is shown and command is $x("//button[@id='login']")
driver.find_element(By.ID,'login').click()
sleep(5)
#close the btowser
driver.quit()

#instructor used
#actual=driver.find_element(By.XPATH,"//h1/span").text

## OR ,by instructor if you don't want to comapre (line 31 to 35 you can use below command also
##driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']")