from selenium import webdriver
from gen_password import *

# Caveats: two-factor authentication, not currently user-friendly
# Facebook thought my account activity was suspicious (it was)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--test-type")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--enable-automation")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.facebook.com/")

email = "drberryisalivinggod@gmail.com"
current_password = "pleasegivemeana"

# Log in to Facebook
print("Logging into Facebook...")
email_field = driver.find_elements_by_xpath("//input[@type='email']")[0]
email_field.send_keys(email)

password_field = driver.find_elements_by_xpath("//input[@id='pass']")[0]
password_field.send_keys(current_password)

log_in_button = driver.find_elements_by_xpath("//input[@id='u_0_2']")[0]
log_in_button.click()

# Change password in Facebook
driver.get("https://www.facebook.com/settings?tab=security&section=password&view")
print("Changing Facebook password...")

new_password = gen_password()

current_password_field = driver.find_elements_by_xpath("//input[@id='password_old']")[0]
current_password_field.send_keys(current_password)

new_password_field = driver.find_elements_by_xpath("//input[@id='password_new']")[0]
new_password_field.send_keys(new_password)

retype_password_field = driver.find_elements_by_xpath("//input[@id='password_confirm']")[0]
retype_password_field.send_keys(new_password)

save_changes_button = driver.find_elements_by_xpath("//input[@value='Save Changes']")[0]
save_changes_button.click()
