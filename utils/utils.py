import requests
import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def reboot_heroku():
    r = requests.delete(f"https://api.heroku.com/apps/{os.getenv('APP_ID')}/dynos/{os.getenv('DYNO_NAME')}",
                        headers={'Authorization': f"Bearer {os.getenv('API_KEY')}",
                                 'Accept': 'application/vnd.heroku+json; version=3'})
    print(r.text)


def delete_cache(driver):
    driver.delete_all_cookies()
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
    time.sleep(2)
    print('deleting cache')
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
    actions.perform()
    time.sleep(5) # wait some time to finish
    driver.close() # close this tab
    driver.switch_to.window(driver.window_handles[0]) # switch back