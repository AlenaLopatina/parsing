from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import time
chrome_options = Options()
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
driver.get("https://www.mvideo.ru/")

driver.find_element_by_class_name('c-btn_close font-icon icon-delete').click()
time.sleep(2)

new_good = driver.find_element_by_xpath(f"//h2[contains(text(),'Новинки')]/../../..")

actions = ActionChains(driver)
actions.move_to_element(new_good)
actions.perform()

next_btn = block.find_element_by_class_name('next-btn')
page = 0
while page < 5:
    next_btn.click()
    page += 1
goods = block.find_elements_by_xpath(".//a[@data-product-info]")[::2]
goods_list = []
new_goods = 0

for good in goods_list:
        good_dict = {'name': good['productName'],
                     'category':good['productCategoryName'],
                     'price': good['productPriceLocal']}
        new += 1
print(goods_list)



