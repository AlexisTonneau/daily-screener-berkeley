import os
import time
import sys
# import argparse
import uvicorn
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import utils.utils

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--proxy-server=%s' % get_proxy_ip()) #IF NEEDED
driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
wait = WebDriverWait(driver, 10)

app = FastAPI()


class RequestLogin(BaseModel):
    username: str
    password: str


@app.get("/")
async def home():
    return "Welcome here !"


@app.post("/")
async def root(body: RequestLogin):
    driver.get("https://calberkeley.ca1.qualtrics.com/jfe/form/SV_3xTgcs162K19qRv")
    time.sleep(2)

    driver.find_element_by_css_selector('.reg').click()
    driver.find_element_by_css_selector('#NextButton').click()
    time.sleep(1)

    driver.find_element_by_css_selector('.reg').click()
    driver.find_element_by_css_selector('#NextButton').click()
    time.sleep(5)

    driver.find_element_by_id('username').send_keys(body.username)
    driver.find_element_by_id('password').send_keys(body.password)
    driver.find_element_by_id('submit').click()
    time.sleep(4)

    if driver.find_elements_by_css_selector('.error'):
        driver.close()
        utils.utils.reboot_heroku()
        return 400, 'BAD USERNAME/PASSWORD'

    try:
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_css_selector('#remember_me_label_text').click()
        time.sleep(0.2)
        driver.find_element_by_css_selector('.push-label button').click()
        wait.until(EC.title_is('UC Berkeley Symptom Tracker'))
    except Exception as e:
        print(e)
        pass

    time.sleep(5)

    driver.get("https://calberkeley.ca1.qualtrics.com/jfe/form/SV_3xTgcs162K19qRv")
    time.sleep(4)
    try:
        driver.find_element_by_css_selector('label#QID3-2-label.SingleAnswer').click()
        driver.find_element_by_css_selector('#QID6-5-label').click()
        driver.find_element_by_css_selector('#QID17-1-label').click()
        driver.find_element_by_css_selector('#QID13-2-label').click()
        driver.find_element_by_css_selector('#NextButton').click()

    except Exception as e:
        print(driver.page_source)
        print(e)
        utils.utils.reboot_heroku()
        return 500, 'An error occurred'

    try:  # For dev purposes
        if sys.argv[1] == "close":
            time.sleep(10)
            driver.close()
    except IndexError:
        pass
    utils.utils.reboot_heroku()


# @app.get("/reboot")
# async def reboot():
#     utils.utils.reboot_heroku()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.getenv('PORT') or 9000)
