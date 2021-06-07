import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options

import speech_recognition as sr
import ffmpy
import requests
import urllib
import pydub
from datetime import datetime

def delay():
    time.sleep(random.randint(2,3))

def myfunc(driver):
    print("myfunc")
    frames = driver.find_elements_by_tag_name('iframe')
    print(frames)
    driver.switch_to.frame(frames[0])
    delay()
    check = driver.find_element_by_class_name("recaptcha-checkbox").click()

    driver.switch_to.default_content()
    frame = driver.find_element_by_css_selector('iframe[title="recaptcha challenge"]')
    driver.switch_to.frame(frame)
    delay()
    # check = driver.find_element_by_class_name("rc-button-audio").click()
    # check = driver.find_element_by_id("recaptcha-audio-button").click()
    driver.find_element_by_id("recaptcha-audio-button").click()
    delay()
    driver.switch_to.default_content()
    frame = driver.find_element_by_css_selector('iframe[title="recaptcha challenge"]')
    driver.switch_to.frame(frame)
    delay()
    src = driver.find_element_by_id("audio-source").get_attribute("src")
    print("[INFO] Audio src: %s" %src )
    print(os.getcwd())
    urllib.request.urlretrieve(src, os.getcwd() + "\\sample.mp3")

    sound = pydub.AudioSegment.from_mp3(os.getcwd() +"\\sample.mp3")
    sound.export(os.getcwd()+"\\sample.wav",format="wav")
    sample_audio = sr.AudioFile(os.getcwd()+"\\sample.wav")
    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)

    key = r.recognize_google(audio)

    print("[INFO] Recaptcha Passcode: %s"%key)
    driver.find_element_by_id("audio-response").send_keys(key.lower())
    driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)

