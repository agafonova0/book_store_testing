from selenium import webdriver
from selenium.webdriver.support.select import Select
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
sorting = driver.find_element_by_css_selector("[value='menu_order']")
sorting_selected = sorting.get_attribute("selected")
if sorting_selected is not None:
    print("Выбрана сортировка по умолчанию")
selector_1 = driver.find_element_by_class_name("orderby")
select = Select(selector_1)
select.select_by_value("price-desc")
selector_2 = driver.find_element_by_css_selector("[value='price-desc']")
selector_2_selected = selector_2.get_attribute("selected")
if selector_2_selected is not None:
    print("Выбрана сортировка цены по убыванию")


