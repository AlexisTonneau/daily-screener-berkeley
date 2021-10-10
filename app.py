import os
import time
import sys
import uvicorn
from fastapi import FastAPI, BackgroundTasks
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

app = FastAPI()


class RequestLogin(BaseModel):
    username: str
    password: str


@app.get("/")
async def home():
    return "Welcome here !"


@app.post("/")
async def root(body: RequestLogin, background: BackgroundTasks):
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
    driver.set_page_load_timeout(50)
    wait = WebDriverWait(driver, 10)
    driver.get("https://calberkeley.ca1.qualtrics.com/jfe/form/SV_3xTgcs162K19qRv")
    time.sleep(1)

    driver.find_element_by_css_selector('.reg').click()
    driver.find_element_by_css_selector('#NextButton').click()
    time.sleep(0.5)

    driver.find_element_by_css_selector('.reg').click()
    driver.find_element_by_css_selector('#NextButton').click()
    time.sleep(2)

    driver.find_element_by_id('username').send_keys(body.username)
    driver.find_element_by_id('password').send_keys(body.password)
    driver.find_element_by_id('submit').click()
    time.sleep(2)

    if driver.find_elements_by_css_selector('.error'):
        driver.close()
        return 400, 'BAD USERNAME/PASSWORD'

    background.add_task(process_in_background, browser=driver, wait=wait)
    return


def process_in_background(browser, wait):
    browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
    time.sleep(0.2)
    browser.find_element_by_css_selector('.push-label button').click()
    wait.until(EC.title_is('UC Berkeley Symptom Tracker'))
    time.sleep(0.3)
    try:
        browser.find_element_by_css_selector('label#QID3-2-label.SingleAnswer').click()
        browser.find_element_by_css_selector('#QID6-5-label').click()
        browser.find_element_by_css_selector('#QID17-1-label').click()
        browser.find_element_by_css_selector('#QID13-2-label').click()
        browser.find_element_by_css_selector('#NextButton').click()

    except Exception as e:
        print(browser.page_source)
        print(e)
        return 500, 'An error occurred'

    try:  # For dev purposes
        if sys.argv[1] == "close":
            time.sleep(10)
            browser.close()
    except IndexError:
        pass

    time.sleep(5)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.getenv('PORT') or 9000)
