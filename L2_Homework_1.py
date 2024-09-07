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
#driver.get("https://www.amazon.com/")
#driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.refresh()
sleep(15)
#command $x("//a[@href='https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0']")
#driver.find_element(By.XPATH,"//a[@href='https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0']") .click()
#for sign in button used  XPATH and command in console  $x("//a[@data-csa-c-content-id='nav_ya_signin']")
#driver.find_element(By.XPATH,"//a[@data-csa-c-content-id='nav_ya_signin']").click()

#command $x("//span[@id='nav-link-accountList-nav-line-1']")
#driver.find_element(By.XPATH,"//span[@id='nav-link-accountList-nav-line-1']").click()

# for amazon logo used XPATH and command in console $x("//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
sleep(6)

#for Email field used ID and to test command in console used  $x("//input[@id='ap_email']")
driver.find_element(By.ID,'ap_email')
sleep(6)

#for Continue Button used ID and command in console $x("//input[@id='continue']")
driver.find_element(By.ID,'continue')

#for Condition of use link used XPATh and command is $x("//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#for Privacy Notice link used XPATH and command is $x("//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")


# for Need help link used XPATH and command is $x("//span[@class='a-expander-prompt']")
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")

#for Forgot your password link used ID and check it in console $x("//a[@id='auth-fpp-link-bottom']")
driver.find_element(By.ID,'auth-fpp-link-bottom')

#for Other issue in sign in link used ID and check it in console $x("//a[@id='ap-other-signin-issues-link']")
driver.find_element(By.ID,'ap-other-signin-issues-link')

#for create your Amazon account button use ID and check it in console $x("//a[@id='createAccountSubmit']")
driver.find_element(By.ID,'createAccountSubmit')

#close the browser
driver.quit()
