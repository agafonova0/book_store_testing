import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(20)

my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
my_account.click()
email = driver.find_element_by_id("reg_email")
email.send_keys("ivanov@gmail.com")
password = driver.find_element_by_id("reg_password")
password.send_keys("Ytp3sh9IB_12U")
register = driver.find_element_by_css_selector(".woocomerce-FormRow > input:nth-child(3)")
register.click()

