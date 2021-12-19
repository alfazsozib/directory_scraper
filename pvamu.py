from typing import Text
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer
from pandas.core.frame import DataFrame
import requests
import pandas as pd
from requests.exceptions import URLRequired
from requests.models import StreamConsumedError
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time





url = 'https://www.pvamu.edu/directory/'
r = requests.get(url)


driver = webdriver.Chrome('E:/Exercies/scrapping/chromedriver.exe')
driver.get(url)
time.sleep(5)

search = driver.find_element_by_xpath('//div[@id="content"]/form/table/tbody/tr[1]/td[2]/input')
time.sleep(10)
search.send_keys('a')
time.sleep(10)