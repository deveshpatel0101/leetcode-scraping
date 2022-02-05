from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.binary_location = "C:\Program Files\BraveSoftware\Brave-Browser\Application"

browser = webdriver.Chrome(
    executable_path="C:/workspace/python/LeetCode-scraping/chromedriver.exe")
browser.maximize_window()
URL = "https://leetcode.com/problemset/all/"
browser.get(URL)
time.sleep(3)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

pages = browser.find_elements(By.CSS_SELECTOR, 'nav button')[11].text
pages = int(pages)

f = open('links.csv', 'w')
f.write('name, link\n')
f.flush()

for index in range(1, pages+1):
    link = f'{URL}?page={index}'
    browser.get(link)
    time.sleep(5)
    elements = browser.find_elements(
        By.CSS_SELECTOR, 'div[role=rowgroup] div[role=row] div[role=cell]:nth-child(2) a')
    for element in elements:
        problem_link = element.get_attribute('href')
        problem_name = element.text.replace(',', '')
        f.write(f'{problem_name}, {problem_link}\n')
        f.flush()
