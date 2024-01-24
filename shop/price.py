import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(10)

my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
my_account.click()
email = driver.find_element_by_id("username")
email.send_keys("petrov@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("123ABC_789xyz!")
login = driver.find_element_by_css_selector(".form-row > input:nth-child(3)")
login.click()
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
add_to_basket = driver.find_element_by_css_selector(".post-182 > .button")
add_to_basket.click()
cart_item = driver.find_element_by_css_selector(".wpmenucart-contents > .cartcontents")
cart_item_get_text = cart_item.text
cart_item_get_text == "1 item"
cart_price = driver.find_element_by_css_selector(".wpmenucart-contents > .amount")
cart_price_get_text = cart_price.text
cart_price_get_text == "₹180.00"
time.sleep(5)
cart = driver.find_element_by_css_selector(".wpmenucart-contents > .cartcontents")
cart.click()
wait = WebDriverWait(driver, 15)
subtotal_price = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal > td > span"), "₹180.00"))
total_price = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total > td > strong > span"), "₹183.60"))

