from typing import Text
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import requests
# import urllib3
# from urllib.parse import quote

from datetime import datetime
# import clipboard
import time
import glob
import json
import os


DRIVER_PATH = '/home/gsoft/chromedriver/96/chromedriver'
BASE_URL = 'https://juicebox.money/#/p/constitutiondao'
BASE_FOLDER = '/media/webguy/ubstrg/permitted_storage/VSCODE_GIT/python-scripts/juicebox_scrap/Downloads/'

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    # prefs = {'download.default_directory':BASE_FOLDER}
    driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=chrome_options )
    return driver


def dev_db(saver_d = {}):
    from db_util import setter_juice
    ret_got = setter_juice(saver_d)
    return ret_got

# # def sanitize_url(string_to_sanitize =''):
# #     return quote(string_to_sanitize)

# def class_name_to_css(class_name):
#     return '.'+class_name.replace(' ','.')

# def pdf_file_download(element_obj, dir_loc = ''):
#     element_obj.click()
#     time.sleep(5)
#     return True

# def run_util(url = BASE_URL, folder_name = BASE_FOLDER):
#     driver = get_driver()
#     driver.get(url)
#     time.sleep(5)
#     # driver.save_screenshot(folder_name+'/'+'screenshot.png')
#     pdfs_elems = driver.find_elements_by_css_selector(class_name_to_css('file'))
#     pdfs_names = [elem.get_attribute('href') for elem in pdfs_elems]
#     for pdf in pdfs_elems:
#         pdf_file_download(pdf, BASE_FOLDER)
#     driver.close()
#     driver.quit()


# # print(sanitize_url('boka bakso.pdf'))
# run_util()

def driver_return():
    driver = get_driver()
    driver.get(BASE_URL)
    driver.implicitly_wait(1)
    time.sleep(20)
    return driver

def get_comments(start_count, end_count, driver):
    for div_index in range(start_count, end_count+1):
        end_loop = False
        if div_index == end_count:
            end_loop = True
        else:
            container_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{div_index}]/div[2]/span/span'
            end_loop = False

        try:
            container_elem = driver.find_element(By.XPATH, container_xpath)
            comment_text = container_elem.text

            amount_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{div_index}]/div[1]/div[1]/div[2]'
            link_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{div_index}]/div[1]/div[2]/div[1]/a'
            amount_elem = driver.find_element(By.XPATH, amount_xpath)
            link_elem = driver.find_element(By.XPATH, link_xpath)
            link_text = link_elem.get_attribute('href')
            amount_text = amount_elem.text
            # print(f'\nidx:{div_index}\nComment:{comment_text}')
            saver_d = {'comment':comment_text, 'amount': amount_text, 'link':link_text}
            dev_db(saver_d)
        except Exception as e:
            # print(e)
            amount_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{div_index}]/div[1]/div[1]/div[2]'
            link_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{div_index}]/div[1]/div[2]/div[1]/a'
            amount_elem = driver.find_element(By.XPATH, amount_xpath)
            link_elem = driver.find_element(By.XPATH, link_xpath)
            link_text = link_elem.get_attribute('href')
            amount_text = amount_elem.text
            saver_d = {'amount': amount_text, 'link':link_text}
            dev_db(saver_d)
        
        if end_loop:
            container_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{end_count+1}]'
            container_elem = driver.find_element(By.XPATH, container_xpath)
            container_elem.click()
            time.sleep(10)

            start_count = end_count+1
            end_count = end_count + 50
            # Call this recursively
            if end_count < 1350:
                get_comments(start_count, end_count, driver)
            else:
                driver.close()

# get_comments(1,50,driver_return())

def get_comments_2(start_count, end_count, driver):
    for div_index in range(start_count, end_count+1):
        print(div_index)
        end_loop = False
        if div_index == end_count:
            end_loop = True
        else:
            container_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{div_index}]/div[2]/span/span'
            end_loop = False
        if start_count > 3400:
            try:
                container_elem = driver.find_element(By.XPATH, container_xpath)
                comment_text = container_elem.text

                amount_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{div_index}]/div[1]/div[1]/div[2]'
                link_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{div_index}]/div[1]/div[2]/div[1]/a'
                amount_elem = driver.find_element(By.XPATH, amount_xpath)
                link_elem = driver.find_element(By.XPATH, link_xpath)
                link_text = link_elem.get_attribute('href')
                amount_text = amount_elem.text
                # print(f'\nidx:{div_index}\nComment:{comment_text}')
                saver_d = {'comment':comment_text, 'amount': amount_text, 'link':link_text}
                dev_db(saver_d)
            except Exception as e:
                # print(e)
                amount_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{div_index}]/div[1]/div[1]/div[2]'
                link_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{div_index}]/div[1]/div[2]/div[1]/a'
                amount_elem = driver.find_element(By.XPATH, amount_xpath)
                link_elem = driver.find_element(By.XPATH, link_xpath)
                link_text = link_elem.get_attribute('href')
                amount_text = amount_elem.text
                saver_d = {'amount': amount_text, 'link':link_text}
                dev_db(saver_d)
            
        if end_loop:
            container_xpath = f'//*[@id="root"]/section/main/div/div[1]/div[3]/div[2]/div/div[2]/div[{end_count+1}]'
            container_elem = driver.find_element(By.XPATH, container_xpath)
            container_elem.click()
            time.sleep(7)

            start_count = end_count+1
            end_count = end_count + 50
            # Call this recursively
            if end_count < 4050:
                get_comments_2(start_count, end_count, driver)
            else:
                driver.close()

get_comments_2(1, 50, driver_return())



