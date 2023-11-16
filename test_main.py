import selenium
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def testurl():
    driver.get(os.getenv('BASEURL'))
    driver.maximize_window()
    page_url: str = driver.current_url
    assert os.getenv('BASEURL') in page_url

    
def testtitle():
    assert 'COMPRESS MASTER' == driver.title, 'unexpected title'


def testcred():
    driver.find_element(By.CSS_SELECTOR, '#file-type').send_keys('FILETYPE')
    driver.find_element(By.CSS_SELECTOR, '#parameter').send_keys('parameter')


time.sleep(10)
