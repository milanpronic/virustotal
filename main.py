from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import random
from myrecapcha import myfunc
def delay():
    time.sleep(random.randint(2,3))
data= pd.read_excel('./test.xlsx')
data = data.drop_duplicates(subset="domain")

driver = webdriver.Chrome()

for domain in data['domain']:
    url = "https://www.virustotal.com/gui/domain/" + domain
    driver.get(url)
    # time.sleep(20)
    capitem = driver.find_element(By.ID, 'captchaContainer')
    if capitem.value_of_css_property('display') == 'block':
        myfunc(driver)
        delay()
        # btn = driver.execute_script("return document.querySelector('item-not-found-view').shadowRoot.querySelector('vt-ui-button').shadowRoot.querySelector('#wrapperLink')")
        input = driver.execute_script("return document.querySelector('vt-ui-shell').shadowRoot.querySelector('vt-ui-search-bar').shadowRoot.querySelector('vt-ui-text-input').shadowRoot.querySelector('#input')")
        input.send_keys(domain)
        input.send_keys(Keys.ENTER)
        delay()
        item = driver.execute_script("return document.querySelector('ip-address-view').shadowRoot.querySelector('vt-ui-main-generic-report').shadowRoot.querySelector('vt-ui-detections-widget').shadowRoot.querySelector('.positives')")
        print(domain + " " + item.text)
    elif driver.find_element(By.TAG_NAME, 'item-not-found-view').value_of_css_property('display') == 'block':
        delay()
        # btn = driver.execute_script("return document.querySelector('item-not-found-view').shadowRoot.querySelector('vt-ui-button').shadowRoot.querySelector('#wrapperLink')")
        input = driver.execute_script("return document.querySelector('vt-ui-shell').shadowRoot.querySelector('vt-ui-search-bar').shadowRoot.querySelector('vt-ui-text-input').shadowRoot.querySelector('#input')")
        input.send_keys(domain)
        input.send_keys(Keys.ENTER)
        delay()
        item = driver.execute_script("return document.querySelector('ip-address-view').shadowRoot.querySelector('vt-ui-main-generic-report').shadowRoot.querySelector('vt-ui-detections-widget').shadowRoot.querySelector('.positives')")
        print(domain + " " + item.text)
    else:
        item = driver.execute_script("return document.querySelector('domain-view').shadowRoot.querySelector('vt-ui-main-generic-report').shadowRoot.querySelector('vt-ui-detections-widget').shadowRoot.querySelector('.positives')")
        print(domain + " " + item.text)
driver.close()