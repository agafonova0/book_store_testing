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
book = driver.find_element_by_css_selector(".post-181 > a")
book.click()
title = driver.find_element_by_class_name("entry-title")
title_get_text = title.text
assert title_get_text == "HTML5 Forms"