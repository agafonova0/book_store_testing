from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(20)

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
item = driver.find_element_by_css_selector(".post-169 > a")
item.click()
old_price = driver.find_element_by_css_selector(".price > del > span")
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"
new_price = driver.find_element_by_css_selector(".price > ins > span")
new_price_get_text = new_price.text
assert new_price_get_text == "₹450.00"
wait = WebDriverWait(driver, 5)
picture = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a")))
picture.click()
close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_details > a")))
close.click()
