from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('C:/Users/ADMIN/Downloads/chromedriver.exe')
driver.get('https://www.whatsapp.com/')
wait = WebDriverWait(driver, 600)
target = 'Target_name'
string = "message sent using python!!!"
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_all_elements_located((By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_all_elements_located((By.XPATH, inp_xpath)))
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)