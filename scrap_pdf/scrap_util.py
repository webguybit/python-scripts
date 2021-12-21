from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import requests
import urllib3
from urllib.parse import quote

from datetime import datetime
# import clipboard
import time
import glob
import json
import os


DRIVER_PATH = '/home/webguy/chromedriver/95/chromedriver'
BASE_URL = 'https://book.kamrul.workers.dev/'
BASE_FOLDER = '/media/webguy/ubstrg/permitted_storage/VSCODE_GIT/python-scripts/scrap_pdf/Downloads/'

def get_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    prefs = {'download.default_directory':BASE_FOLDER}
    driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=chrome_options )
    return driver

def sanitize_url(string_to_sanitize =''):
    return quote(string_to_sanitize)

def class_name_to_css(class_name):
    return '.'+class_name.replace(' ','.')

def pdf_file_download(element_obj, dir_loc = ''):
    element_obj.click()
    time.sleep(5)
    return True

def run_util(url = BASE_URL, folder_name = BASE_FOLDER):
    driver = get_driver()
    driver.get(url)
    time.sleep(5)
    # driver.save_screenshot(folder_name+'/'+'screenshot.png')
    pdfs_elems = driver.find_elements_by_css_selector(class_name_to_css('file'))
    pdfs_names = [elem.get_attribute('href') for elem in pdfs_elems]
    for pdf in pdfs_elems:
        pdf_file_download(pdf, BASE_FOLDER)
    driver.close()
    driver.quit()



# print(sanitize_url('boka bakso.pdf'))
run_util()