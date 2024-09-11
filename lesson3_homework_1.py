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


# open the amazon registration page url "https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_logo%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_logo%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.refresh()
sleep(10)

# Locator for 'amazon logo' on registration page using multiple class and attribute  and used command on console $$(".a-icon.a-icon-logo[aria-label='Amazon']")
driver.find_element(By.CSS_SELECTOR,".a-icon.a-icon-logo[aria-label='Amazon']")
sleep(5)

#Locator for 'Create Account' using tag-name and class and command is $$("h1.a-spacing-small")
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")
sleep(5)

#Locator for 'your name box' using id and attribute and used command  $$("#ap_customer_name[placeholder='First and last name']").only attribute also worked
driver.find_element(By.CSS_SELECTOR,"#ap_customer_name[placeholder='First and last name']")
sleep(5)

#Locator for 'email box' used multiple attribute and command $$("[name='email'][type='email']")
driver.find_element(By.CSS_SELECTOR,"[name='email'][type='email']")
sleep(5)

#Locator for 'password box' used multiple classes and multiple attribute and command is $$(".a-input-text.auth-required-field[type='password'][name='password']")
driver.find_element(By.CSS_SELECTOR,".a-input-text.auth-required-field[type='password'][name='password']")
sleep(5)

#Locator for 'i password must be at least 6 character  meassage '  ,used parent id and child attribute and command $$("#ap_password_context_message_section [aria-live='polite']")
driver.find_element(By.CSS_SELECTOR,"#ap_password_context_message_section [aria-live='polite']")
sleep(5)

#Locator for 'Reenter password box' used partial parent class  and child id and command is $$("[class*='a-spacing-base'] #ap_password_check ")
driver.find_element(By.CSS_SELECTOR,"[class*='a-spacing-base'] #ap_password_check ")
sleep(5)

#Locator for 'continue' as I dont have 'create amazon account' in my web page. used tag name,id ,class and command $$("input#continue.a-button-input")
driver.find_element(By.CSS_SELECTOR,"input#continue.a-button-input")
sleep(5)

#Locator for 'Condition of use ' used parent id and partial href attribute and command $$("#legalTextRow [href*='ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR,"#legalTextRow [href*='ap_register_notification_condition_of_use']")

#Locator for 'Privacy Notice ' used parent id and partial href attributeand command $$("#legalTextRow [href*='privacy_notice']")
driver.find_element(By.CSS_SELECTOR,"#legalTextRow [href*='privacy_notice']")

#Locator for 'sign in'  used parent class and child class  and command $$(".a-row .a-link-emphasis")
driver.find_element(By.CSS_SELECTOR,".a-row .a-link-emphasis")