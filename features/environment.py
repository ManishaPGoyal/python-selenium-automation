from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from app.application import Application



#def browser_init(context):
#use below when use Browserstack
def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    #fFirefox Driver code also need to import webDivermanager.firefox
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    #for Safari browser and also enable remote automation in developer setting of safari
    #context.driver=webdriver.Safari()

    ## browser with physical driver
    # service=Service(executable_path='')
    # context.driver=webdriver.Firefox(service=service)

    ##Headless browser##
    # options=webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service=Service(ChromeDriverManager().install())
    # context.driver=webdriver.Chrome(service=service,options=options)
#homework 8 part 2
#using Browserstack
# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = ''
    bs_key = ''
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "os" : "Windows",
        "osVersion" : "11",
        'browserName': 'edge',
        'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app=Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    #browser_init(context)
    #use belpw when use Browserstack
    browser_init(context,scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
