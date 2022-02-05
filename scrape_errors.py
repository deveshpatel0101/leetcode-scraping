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

links = []
f = open('errors.txt')
for line in f.readlines():
    links.append(line.strip('\n'))
f.close()

total = len(links)
errors = []

data_file = open('data.csv', 'a')
error_file = open('errors.txt', 'w')

for i, link in enumerate(links):
    try:
        print(f"{i+1}/{total}", end=" ")
        browser.get(link)
        time.sleep(4.5)
        buttons = browser.find_elements(By.TAG_NAME, "button")
        difficulty_level = browser.find_elements(By.CLASS_NAME, "css-dcmtd5") + browser.find_elements(By.CLASS_NAME,
                                                                                                      "css-t42afm") + browser.find_elements(By.CLASS_NAME, "css-14oi08n")
        submitted = browser.find_elements(By.CLASS_NAME, "css-jkjiwi")

        likes = buttons[1].text
        dislikes = buttons[2].text
        difficulty_level = difficulty_level[0].text
        accepted = submitted[0].text.replace(",", "")
        total_submissions = submitted[1].text.replace(",", "")
        acceptance = round(int(accepted) / int(total_submissions), 2)
        line = f'{link}, {likes}, {dislikes}, {difficulty_level}, {accepted}, {total_submissions}, {acceptance}\n'
        data_file.writelines([line])
        data_file.flush()
        print(f"Visited : {link}")
    except:
        print(f"Error while visiting : {link}")
        error_file.writelines([f'{link}\n'])
        error_file.flush()

browser.close()
