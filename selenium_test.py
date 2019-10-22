from sys import argv
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--test-type")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--enable-automation")
chrome_options.binary_location = "/usr/bin/chromium" # May not work on Windows
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://codepad.org")

# click radio button
python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
python_button.click()

# type text
text_area = driver.find_element_by_id("textarea")
text_area.send_keys("print('Hello world')")

# click submit button
submit_button = driver.find_elements.by_xpath('//*[@id="editor"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')[0]
submit_button.click()

if len(argv) == 2 and argv[1] == "--no-close":
    print("Keeping browser window open...")
else:
    driver.close()
