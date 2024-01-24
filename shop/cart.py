import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(20)

shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
driver.execute_script("window.scrollBy(0,300);")
item_1 = driver.find_element_by_css_selector(".post-182 > .button")
item_1.click()
time.sleep(5)
item_2 = driver.find_element_by_css_selector(".post-180 > .button")
item_2.click()
time.sleep(5)
basket = driver.find_element_by_css_selector(".wpmenucart-contents > .cartcontents")
basket.click()
time.sleep(5)
delete = driver.find_element_by_css_selector(".product-remove:nth-child(1) > a")
delete.click()
undo = driver.find_element_by_css_selector(".woocommerce-message > a")
undo.click()
quantity = driver.find_element_by_css_selector(".quantity:nth-child(1) > input")
quantity.clear()
quantity.send_keys("3")
update = driver.find_element_by_css_selector(".actions > .button")
update.click()
quantity_value = quantity.get_attribute("value")
assert quantity_value == "3"
time.sleep(5)
coupon = driver.find_element_by_css_selector(".coupon > .button")
coupon.click()
message = driver.find_element_by_css_selector(".woocommerce-error > li")
message_get_text = message.text
assert message_get_text == "Please enter a coupon code."



