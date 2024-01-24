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
html = driver.find_element_by_css_selector(".cat-item-19 > a")
html.click()
items_count = driver.find_elements_by_class_name("product")
if len(items_count) == 3:
    print("На странице отображается 3 товара")
else:
    print("Ошибка. Количество товаров на странице: " + str(len(items_count)))